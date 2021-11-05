# dalec-openproject

Django Aggregate a Lot of External Content -- OpenProject

Aggregate last event from a given OpenProject instance.

Plugin of [dalec](https://dev.webu.coop/w/i/dalec).

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

### Events

Retrieves latest events:
```django
{% dalec "openproject" "event" %}
```


## Settings

Django settings must define:

  - `DALEC_OPENPROJECT_BASE_URL` : OpenProject instance url (ex: `https://openproject.org/`)
  - `DALEC_OPENPROJECT_API_KEY` : OpenProject api key (ex: `admazerazerazerazerazer`)

