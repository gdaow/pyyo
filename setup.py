"""PyYO installation configuration."""

from setuptools import setup

setup(
    name="PyYO",
    version="0.1",
    packages=['pyyo'],
    install_requires=[
        'pyyaml'
    ],
    author="Corentin Séchet",
    author_email="corentin@ki-dour.org",
    description="Python Yaml Object deserializer based on PyYAML",
    url="http://github.com/corentin/pyyo/",
)
