"""PyYO installation configuration."""

from setuptools import setup

setup(
    name="PyYO",
    description="Python Yaml Object deserializer based on PyYAML.",
    long_description=(
        "Python Yaml Object deserializer based on PyYAML. " +
        "Allow to defines schema in python code directly, and provides " +
        "automatic validation."),
    version="0.1",
    keywords=['YAML', 'serialization'],
    packages=['pyyo'],
    license='WTFPL',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],
    install_requires=['pyyaml'],
    author="Corentin Séchet",
    author_email="corentin@ki-dour.org",
    url="http://github.com/corentin/pyyo/",
    zip_safe=False,
)
