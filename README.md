[![Build Status](https://travis-ci.org/tobse80/rof-helpers.svg?branch=master)](https://travis-ci.org/tobse80/rof-helpers)
[![Python package](https://github.com/tobse80/rof-helpers/workflows/Python%20package/badge.svg)](https://github.com/tobse80/rof-helpers/actions?query=workflow%3A%22Python+package%22)

# rof-helpers

Helper functions supporting tests written for Robot Framework.

## Structure

| directory     | purpose
| --------------| -------
| `src`         | python source code implementing rof-helper modules
| `tests`       | pytest code for testing rof-helper modules
| `rof-samples` | RoF samples utilizing rof-helper modules

## Running tests

### PyTest

In the project's top directory, open a command shell and run:

```sh
pytest
```

### Robot Framework samples

In the project's top directory, open a command shell and run:

```sh
robot --pythonpath src rof-samples
```

## Building distribution packages

In the project's top directory, open a command shell and run:

```sh
python3 setup.py sdist bdist_wheel
```
