from setuptools import setup, find_packages

setup(
    name="PIP_LIB",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="UOM",
    author_email="sowndaraya25@gmail.com",
    description="A simple example private package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SowndaryaC09/PIP_LIB",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)