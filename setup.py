from setuptools import setup

setup(name='RobotCar',
      version='0.9.0',
      packages=['robotcar'],
      entry_points={
          'console_scripts': [
              'robotcar = robotcar.__main__:main'
          ]
      },
      )
