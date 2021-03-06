# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

packages = find_packages(exclude=['tests*'])


# Taken from https://github.com/python-telegram-bot/python-telegram-bot/blob/9d99660ba95b103b3e1dc80414a5ce2fd805260b/setup.py#L9
def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as reqs:
        for install in reqs:
            requirements_list.append(install.strip())

        return requirements_list


with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

version_file = os.path.join('pastepwn', 'version.txt')
with open(version_file, "r", encoding="utf-8") as file:
    version = file.readline()

setup(name='pastepwn',
      version=version,
      install_requires=requirements(),
      keywords='python pastebin scraping osint framework',
      description='Python framework to scrape PasteBin pastes and analyze them',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/d-Rickyy-b/pastepwn',
      author='d-Rickyy-b',
      author_email='pastepwn@rickyy.de',
      license='MIT',
      packages=packages,
      include_package_data=True)
