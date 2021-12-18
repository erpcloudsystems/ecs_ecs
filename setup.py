from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecs_ecs/__init__.py
from ecs_ecs import __version__ as version

setup(
	name="ecs_ecs",
	version=version,
	description="ecs customizations",
	author="erpcloud.systems",
	author_email="info",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
