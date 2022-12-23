from os import path
from setuptools import setup, find_packages

try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None

try:
    with open (path.join(current_path, 'README.txt'), mode='r',
            encoding='utf-8',) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='package',
    version=0.4,
    license='MIT License',
    author='Alexandr Gopienko',
    author_email='sagopien04@mail.ru',
    description='Test project',
    long_description=long_description,
    packages=find_packages(),
    long_description_content_type='test/markdown',
    python_requires='>=3.5',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'bar=t_package:main',
            'foo=t_package.foo:some_func',
        ],
    },
)