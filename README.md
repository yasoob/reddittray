RedditTray
==========

RedditTray is a simple [Reddit](https://reddit.com/r/python) Linux application
that lets you view /r/python links in your System Tray. It currently supports python only 
however I will add an option to add other subreddits as well It relies on appindicator, so
it is not guaranteed to work on all systems. It also provides a Gtk StatusIcon fallback
in case AppIndicator is not available.

The inspiration for this came from [hackertray](https://github.com/captn3m0/hackertray), which is 
for Hacker news. I just ported that code for reddit.

##Screenshot

![RedditTray Screenshot in Ubuntu](http://i.imgur.com/gzIXbzW.png)

##Installation
RedditTray is distributed as a python package. Do the following to install:

``` sh
sudo pip install reddittray
OR
sudo easy_install reddittray
OR
#Download Source and cd to it
sudo python setup.py install
```

After that, you can run `reddittray` from anywhere and it will run. You can
now add it to your OS dependent session autostart method. In Ubuntu, you can
access it via: 

1. System > Preferences > Sessions  
(OR)
2. System > Preferences > Startup Applications 

depending on your Ubuntu Version. Or put it in `~/.config/openbox/autostart` 
if you are running OpenBox. 

###Upgrade
The latest stable version is always the one [available on pip](https://pypi.python.org/pypi/reddittray/).
You can check which version you have installed with `pip freeze | grep reddittray`.

To upgrade, run `pip install -U reddittray`. In some cases (Ubuntu), you might
need to clear the pip cache before upgrading:

`sudo rm -rf /tmp/pip-build-root/reddittray`

##Features
1. Minimalist Approach to HN
2. Opens links in your default browser
3. Remembers which links you opened
4. Shows Points/Comment count in a simple format

##To-Do
- Auto Start
- Try to convert right click to reddit link

##Author Information
- Muhammad Yasoob Khalid (<yasoob.khld@gmail.com>)

##Licence
Licenced under the MIT Licence