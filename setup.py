from codecs import open
from os import path
from setuptools import setup

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="rpi-tlc59711",
    version="1.0.0",
    description="Raspberry Pi library to communicate with the TLC59711 12 channel LED driver",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Liriel/tlc59711",
    author="Lassi",
    author_email="lassi@heisl.org",
    license="BSD",
    packages=["tlc59711"],
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
    },
)
