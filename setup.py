from setuptools import setup, find_packages

setup(
    name="etl_olympic_project",
    version="0.0.1",
    packages=find_packages(exclude=("tests",)),
    install_requires=[

    ],
    include_package_data=True
)