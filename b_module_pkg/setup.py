from setuptools import setup, find_namespace_packages

setup(
    name='b_module_pkg',
    version='b_module-v0.1-hjchung0918',
    description='b AI model',
    url='',
    author='Gracechung-sw',
    author_email='hjngy0511@gmail.com',
    packages=find_namespace_packages(include=['mynamespace.*']),
    zip_safe=False,
)