# coding: utf-8

from setuptools import setup, find_packages
from html_elmt import __author__, __version__, __license__
 
setup(
        name             = 'html_elmt',
        version          = __version__,
        description      = 'A pip package that obtains a list of class names and ID names written in HTML.',
        license          = __license__,
        author           = __author__,
        url              = 'https://github.com/kazusapon/html_elmt.git',
        packages         = find_packages(),
        install_requires = ['html.parser'],
        )