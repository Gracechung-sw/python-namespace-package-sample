from setuptools import setup, find_namespace_packages

setup(
    name='common_pkg',
    version='0.1',
    description='common AI analyzer utils',
    url='',
    author='Gracechung-sw',
    author_email='hjngy0511@gmail.com',
    packages=find_namespace_packages(include=['mynamespace.*']),
    zip_safe=False,
)
