# dalec-openproject

Django Aggregate a Lot of External Content -- OpenProject

Aggregate last work packages from a given OpenProject instance.

Plugin of [dalec](https://github.com/webu/dalec).

## Installation

```
pip install dalec_openproject
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

