from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in automobile_sales/__init__.py
from automobile_sales import __version__ as version

setup(
	name="automobile_sales",
	version=version,
	description="Automobile Sales App",
	author="Hashim",
	author_email="hashimdreamzz@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
