from setuptools import setup
from setuptools import find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

packages = find_packages()

setup(
    name="yamldict",
    version="1.2.1",
    description="yamldict",
    long_description=readme,
    author="Bogdan Mustiata",
    author_email="bogdan.mustiata@gmail.com",
    license="BSD",
    install_requires=[
        "PyYAML>=5.1.2",
    ],
    packages=packages,
    package_data={
        "": ["*.txt", "*.rst"],
        "yamldict": ["py.typed"],
    },
)
