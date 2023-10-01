from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_payment/__init__.py
from erp_payment import __version__ as version

setup(
	name="erp_payment",
	version=version,
	description="A payment app for bangladesh",
	author="Shaid Azmin",
	author_email="azmin@pixfar.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
