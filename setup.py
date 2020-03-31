from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rof-helpers',
    version='0.0.1',
    description='Helper functions for Robot Framework',
    long_description=readme,
    author='tobse80',
    author_email='tobse.unique@gmail.com',
    url='https://github.com/tobse80/rof-helpers',
    license=license,
    packages=find_packages(exclude=('tests'))
)
