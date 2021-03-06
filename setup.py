from distutils.core import setup

setup(
    name='gtfstk',
    version='6.1.0',
    author='Alex Raichev',
    packages=['gtfstk', 'tests'],
    url='https://github.com/araichev/gtfstk',
    license='LICENSE',
    description='A Python 3.5 tool kit for processing General Transit Feed Specification (GTFS) data',
    long_description=open('README.rst').read(),
    install_requires=[
        'Shapely>=1.5.1,<1.6',
        'pandas>=0.18.1,<0.20',
        'utm>=0.3.1',    
    ],
)

