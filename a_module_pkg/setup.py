from setuptools import setup, find_namespace_packages

setup(
    name='a_module_pkg',
    version='a_module-v0.1-hjchung0919',
    description='a AI model',
    url='',
    author='Gracechung-sw',
    author_email='hjngy0511@gmail.com',
    packages=find_namespace_packages(include=['mynamespace.*']),
    zip_safe=False,
)
