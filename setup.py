import setuptools

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='rof-helpers',
    version='0.1.0',
    description='Helper functions for Robot Framework',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='tobse80',
    author_email='tobse.unique@gmail.com',
    url='https://github.com/tobse80/rof-helpers',
    license=license,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
