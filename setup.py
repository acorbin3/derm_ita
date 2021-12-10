from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="derm_ita",
    version="0.0.1",
    author="Adam Corbin",
    author_email="acorbin3@gmail.com",
    description="A package with different strategies to compute individual typology angle",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/acorbin3/derm_ita",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: The MIT License (MIT)",
    ],
)