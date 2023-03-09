import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "parselib",
    version = "0.0.1a",
    author = "Marcus Antonelli",
    author_email = "marcus.an38@gmail.com",
    description = ("A simple package used to lex, parse, and interpret input-- with support for UDLs."),
    license = "GPLv3",
    keywords = "parsing lexing interpreting microlanguages UDLs",
    url = "https://github.com/marcus-a38/parselib",
    packages=['lexerparser', 'makefile'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Lexing/Parsing/Interpreting",
        "License :: OSI Approved :: GPLv3 License",
    ],
)

# To be edited ...
