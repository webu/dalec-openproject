# Content returned by dalec_openproject

Every dalec save in database object with the following attributes:

 - `last_update_dt` 
 - `creation_dt` 
 - `app` 
 - `content_type` 
 - `channel` 
 - `channel_object` 
 - `dj_channel_content_type_id`
 - `dj_channel_id`
 - `dj_content_content_type_id`
 - `dj_content_id`
 - `content_id`
 - `content_data`

See [the main dalec](https://github.com/webu/dalec) repository for more information.
Hereafter are detailed the `content_data`, specific to the `openproject` content type.

## Work package

```json
{
  // Content returned by the `projects/{project_id}/work_packages` endpoint
  "todo": "fixme"
  // Added by the Dalec
  "id": "string",
  "work_package_url": "string",
  "assignee": "string",
  "project": {"project_url": "string"},
  "created_at": "string",
  "last_update_dt": "string"
}
```
