# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname

requirements = open(join(dirname(__file__), 'requirements.txt')).readlines()
requirements = tuple(map(lambda x: x.strip(), requirements))

setup(
    name='apirequests',
    version='0.0.6',
    packages=find_packages(),
    author='san4ez',
    url='https://github.com/alexandr-san4ez/apirequests',
    description='HTTP client built around "requests" library',
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=requirements,
    test_suite='tests',
    keywords='HTTP API REST HTTP-client requests',
    license='MIT',
)
