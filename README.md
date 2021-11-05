# dalec-openproject

Django Aggregate a Lot of External Content -- CalDav

Aggregate last event from a given CalDav instance.

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

  - `DALEC_CALDAV_BASE_URL` : CalDav instance url (ex: `https://openproject.org/`)
  - `DALEC_CALDAV_API_USERNAME` : CalDav username (ex: `admin`)
  - `DALEC_CALDAV_API_PASSWORD` : CalDav user password (ex: `azeazeaezdfqsmlkrjzr`)


