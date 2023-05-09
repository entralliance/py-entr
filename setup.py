from setuptools import setup, find_packages
from pathlib import Path

def read_file(filename):
    this_directory = Path(__file__).resolve().parent
    with open(this_directory / filename, encoding="utf-8") as f:
        f_text = f.read()
    return f_text

REQUIRED = [
    "pyhive",
    "pyspark",
    "pandas",
    "openoa"
]

TESTS = [
    "pytest",
    "pytest-cov"
]

setup(
    name="entr",
    version="0.0.1",
    description="The ENTR Alliance's python package to load data from an ENTR Warehouse to perform analysis on these data using OpenOA.",
    long_description=read_file("readme.md"),
    long_description_content_type="text/markdown",
    author="ENTR Alliance",
    author_email="",
    url="https://github.com/entralliance/py-entr",
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    install_requires=REQUIRED,
    test_requires=TESTS,
    python_requires=">=3.9"
)
