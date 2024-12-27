# hrid
Generate human readable ids using python.

<!-- toc start -->
## Table of Contents

- [hrid](#hrid)
  - [Purpose](#purpose)
  - [Installation](#installation)
  - [Development](#development)

<!-- toc end -->

## Purpose

Heavily inspired by [Asana's naming scheme](https://asana.com/inside-asana/6-sad-squid-snuggle-softly), this package contains the tools to generate random phrases that represent nearly-unique ids for objects.

## Installation

This package is currently in development and must be installed using a dev install:

```
git clone git@github.com:evelyn-king/hrid.git
cd hrid
python -m pip install -e ".[all]"
```

## Development

This packages uses [`pre-commit`](https://pre-commit.com/) to manage pre-commit hooks, which helps to ensure the code is clean and up-to-date with our coding standards. To set it up, get pre-commit using pip and then run the installer:

```bash
python -m pip install pre-commit
pre-commit install
```
