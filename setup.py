# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in newblack_theme/__init__.py
from newblack_theme import __version__ as version

setup(
	name='newblack_theme',
	version=version,
	description='Theme making for erpnext version-13',
	author='Pranav C',
	author_email='pranav.chandran@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
