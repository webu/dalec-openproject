# 🔗 dalec-openproject

[![Stable Version](https://img.shields.io/pypi/v/dalec-openproject?color=blue)](https://pypi.org/project/dalec-openproject/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![semver](https://img.shields.io/badge/semver-2.0.0-green)](https://semver.org/)

Django Aggregate a Lot of External Content -- OpenProject

Aggregate last work packages from a given OpenProject instance.

Plugin of [🤖 dalec](https://github.com/webu/dalec).

## Installation

```
pip install dalec-openproject
```

In django settings `INSTALLED_APPS`, add:

```
INSTALLED_APPS = [
    ...
    "dalec",
    "dalec_prime",
    "dalec_openproject",
    ...
    ]
```


## Usage

General usage:
```django
{% load dalec %}

{% dalec "openproject" content_type [channel=None] [channel_object=None] [template=None] %}
```

Real examples:

### Work packages

Retrieves latest work packages of a project defined by its identifier (i.e. slug):

```django
{% dalec "openproject" "work_package" channel="project" channel_object="project-identifier"%}
```


## Settings

Django settings must define:

  - `DALEC_OPENPROJECT_BASE_URL` : OpenProject instance url (ex: `https://openproject.org/`)
  - `DALEC_OPENPROJECT_API_KEY` : OpenProject api key (ex: `admazerazerazerazerazer`)

