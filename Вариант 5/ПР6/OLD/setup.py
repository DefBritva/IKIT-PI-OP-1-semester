from os import path
from setuptools import setup

try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None
try:
    with open(path.join(current_path, 'README.md'),
              encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''
setup(
    name='calc_happy',
    version='1.0.1',
    # list folders, not files
    packages=['calc_happy',
              'calc_happy.test'],
    scripts=['calc_happy/bin/calc_happy_script.py',
             'calc_happy/test/test_happy_numbers.py'],
    license='MIT License',
    description='Calculating happy numbers project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    requires=['pytest'],
)
