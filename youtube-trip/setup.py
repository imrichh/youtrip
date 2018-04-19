from setuptools import setup

setup(name='youtube-trip',
      version='0.1',
      description="Randomly picks one of the suggested youtube videos. Repeats forever (if you want)",
      long_description='Enter youtube video, enter how many steps you want to make into the rabbit hole. Sit back and watch where it leads. It also creates a log file of your journey.',
      classifiers=[],
      keywords='youtube rabbit hole suggested videos',
      author='Imrich Valach',
      author_email='nightcrawler@centrum.sk',
      url='https://www.youtube.com/watch?v=oHg5SJYRHA0',
      license='MIT', # or any license you think is relevant
      packages=['motion_control'],
      zip_safe=False,
      install_requires=[
          # add here any tool that you need to install via pip 
          # to have this package working
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      runstepper = motion_control.mystepper6:main
      moveit = motion_control.moveit:main
      """,
)
