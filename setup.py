# setup.py
from setuptools import setup, find_packages

setup(
    name="mathtools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    author="Kittipos Sirivongrungson",
    author_email="your.email@example.com",
    description="A tutorial package for learning Sphinx documentation",
    keywords="math, tools, tutorial",
    url="https://github.com/yourusername/sphinx-tutorial-basic",
)