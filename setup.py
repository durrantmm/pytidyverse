
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytidyverse',
    version='0.0.1.dev1',
    description='A simple python wrapper to easily import packages that were designed to syntactically mimic the '
                'R tidyverse',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/durrantmm/pytidyverse',
    author='Matt Durrant',
    author_email='matthewgeorgedurrant@gmail.com',
    keywords='tidyverse dplython dplyr tidypython tidyr ggplot readr readpy R syntax',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required,
    install_requires = [
        'dplython',
        'ggplot',
        'tidypython',
        'readpy'
    ]
)