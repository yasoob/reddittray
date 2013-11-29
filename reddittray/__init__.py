#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk

import requests
import webbrowser
import json

from os.path import expanduser

try:
    import appindicator
except ImportError:
    import appindicator_replacement as appindicator

class RedditApp:
	def __init__(self):
		#Load the database
		home = expanduser("~")
		with open(home+'/.reddittray.json', 'a+') as content_file:
			content_file.seek(0)
			content = content_file.read()
			try:
				self.db = set(json.loads(content))
			except:
				self.db = set()

		# create an indicator applet
		self.ind = appindicator.Indicator ("Reddit Tray", "reddit-tray", appindicator.CATEGORY_APPLICATION_STATUS)
		self.ind.set_status (appindicator.STATUS_ACTIVE)
		self.ind.set_label("R")

		# create a menu
		self.menu = gtk.Menu()

		# create items for the menu - refresh, quit and a separator
		menuSeparator = gtk.SeparatorMenuItem()
		menuSeparator.show()
		self.menu.append(menuSeparator)

		btnAbout = gtk.MenuItem("About")
		btnAbout.show()
		btnAbout.connect("activate", self.showAbout)
		self.menu.append(btnAbout)

		btnRefresh = gtk.MenuItem("Refresh")
		btnRefresh.show()
		btnRefresh.connect("activate", self.refresh)
		self.menu.append(btnRefresh)

		btnQuit = gtk.MenuItem("Quit")
		btnQuit.show()
		btnQuit.connect("activate", self.quit)
		self.menu.append(btnQuit)

		self.menu.show()

		self.ind.set_menu(self.menu)
		self.refresh()

	'''Handle the about btn'''
	def showAbout(self, widget):
		webbrowser.open("https://github.com/yasoob/reddittray/")

	''' Handler for the quit button'''
	#ToDo: Handle keyboard interrupt properly
	def quit(self, widget, data=None):
		l=list(self.db)
		home = expanduser("~")
		#truncate the file
		file = open(home+'/.reddittray.json', 'w+')
		file.write(json.dumps(l))
		gtk.main_quit()

	def run(self):
		gtk.main()
		return 0

	'''Opens the link in the web browser'''
	def open(self, widget, event=None, data=None):
		#We disconnect and reconnect the event in case we have
		#to set it to active and we don't want the signal to be processed
		if(widget.get_active() == False):
			widget.disconnect(widget.signal_id)
			widget.set_active(True)
			widget.signal_id = widget.connect('activate', self.open)
		self.db.add(widget.item_id)
		webbrowser.open(widget.url)

	'''Adds an item to the menu'''
	def addItem(self, item):
		if len(item['data']['title']) > 57:
			item['data']['title'] = item['data']['title'][:57]+"..."
		i = gtk.CheckMenuItem("("+str(item['data']['score']).zfill(3)+"/"+str(item['data']['num_comments']).zfill(3)+")    "+item['data']['title'])
		i.set_active(item['data']['id'] in self.db)
		i.url = item['data']['url']
		i.signal_id = i.connect('activate', self.open)
		i.item_id = item['data']['id']
		self.menu.prepend(i)
		i.show()

	'''Refreshes the menu '''
	def refresh(self, widget=None, data=None):
		data = getHomePage()
		#Remove all the current stories
		for i in self.menu.get_children():
			if(hasattr(i,'url')):
				self.menu.remove(i)
		#Add back all the refreshed news
		for i in reversed(data['data']['children']):
			self.addItem(i)
		#Call every 5 minutes
		gtk.timeout_add(5*60*1000, self.refresh)

'''Returns all the news stories from homepage'''
def getHomePage():
	r = requests.get('http://www.reddit.com/r/Python.json')
	return r.json()

def main():
	indicator = RedditApp()
	indicator.run()

