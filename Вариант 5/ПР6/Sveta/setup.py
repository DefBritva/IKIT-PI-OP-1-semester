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
    name='bubble_sort',
    version='1.0',
    packages=['bubble_sort',
              'bubble_sort.test'],
    scripts=['bubble_sort/bin/bubble_sort_script.py',
             'bubble_sort/test/test_bubble_sort.py'],
    license='MIT License',
    description='Программа для сортировки чисел методом прямого обмена (пузырьковая сортировка)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    requires=['pytest'],
)
