from setuptools import setup

setup(name='reddittray',
      version='1.5',
      description='Reddit app that sits in your System Tray',
      long_description='RedditTray is a simple Reddit Linux application that lets you view /r/python links in your System Tray. It relies on appindicator, so it is not guaranteed to work on all systems. It also provides a Gtk StatusIcon fallback in case AppIndicator is not available.',
      keywords='reddit news hn tray system tray icon reddittray',
      url='http://github.com/yasoob/reddittray',
      author='Yasoob Khalid',
      author_email='yasoob.khld@gmail.com',
      license='MIT',
      packages=['reddittray'],
      package_data={'reddittray': ['../images/reddit-tray.png']},
      include_package_data=True,
      install_requires=[
          'requests',
      ],
      entry_points={
          'console_scripts': ['reddittray = reddittray:main'],
      },
      zip_safe=False)
