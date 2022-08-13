[![linter-check](https://github.com/Polyrom/python-project-lvl2/actions/workflows/linter-check.yml/badge.svg)](https://github.com/Polyrom/python-project-lvl2/actions/workflows/linter-check.yml) [![tests](https://github.com/Polyrom/python-project-lvl2/actions/workflows/tests.yml/badge.svg)](https://github.com/Polyrom/python-project-lvl2/actions/workflows/tests.yml) [![Actions Status](https://github.com/Polyrom/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Polyrom/python-project-lvl2/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/9b32813f01e693ec86b8/maintainability)](https://codeclimate.com/github/Polyrom/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/9b32813f01e693ec86b8/test_coverage)](https://codeclimate.com/github/Polyrom/python-project-lvl2/test_coverage)

# Gendiff

#### Command line utility to get fast and nicely-formatted difference between two json or yaml files of any complexity


## Quick start
To start out, run the following command in your command line while in the package directory.

```make package-install```

Now you are ready to go!

## Basic usage

The utility's syntax is extremely simple: just specify two paths to the files you would like to compare. Here is a basic example:

```gendiff foo/filename.yml bar/filename.json```

You can choose between three output formats by adding one of the following flags:

* stylish _(default)_
* plain
* json

Example:

```gendiff --f plain foo/filename.yml bar/filename.json```

To see the help page in your command line, run:

```gendiff -h``` or ```gendiff --help```

## Tutorial

[![asciicast](https://asciinema.org/a/eqXcJLHfDn1sMt3kmp1OUHmFn.svg)](https://asciinema.org/a/eqXcJLHfDn1sMt3kmp1OUHmFn)