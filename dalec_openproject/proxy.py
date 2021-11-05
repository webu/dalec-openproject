from datetime import timedelta
from typing import Dict
import requests

from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
from django.conf import settings

from dalec.proxy import Proxy

from pyopenproject.openproject import OpenProject
from pyopenproject.model.project import Project

client = OpenProject(
        url=settings.DALEC_OPENPROJECT_BASE_URL,
        apikey=settings.DALEC_OPENPROJECT_API_KEY,
        )


class OpenprojectProxy(Proxy):
    """
    openproject dalec proxy to fetch the last event.
    """

    app = "openproject"

    def _fetch(
        self, nb: int, content_type: str, channel: str, channel_object: str
    ) -> Dict[str, dict]:
        if content_type == "work_package":
            return self._fetch_work_packages(nb, channel, channel_object)

        raise ValueError(f"Invalid content_type {content_type}. Accepted: work_package." )

    def _fetch_work_packages(self, nb, channel=None, channel_object=None):
        """
        Get latest work packages
        """
        options = {
                "per_page": nb,
                }
        
        if channel != "project":
            raise ValueError(
                    f"""
                    channel is invalid for work_package. It must be : project .
                    """
                    )

        project_identifier = channel_object
        
        project = Project({"identifier": project_identifier})

        project_service = client.get_project_service()
        work_packages = project_service.find_work_packages(project)

        contents = {}
        for wp in work_packages:
            content = {
                    attr: getattr(wp, attr)
                    for attr in dir(wp)
                    if not attr.startswith("__")
                    }
            content.update(
                    {
                        "id": str(wp.id),
                        "creation_dt": wp.createdAt,
                        "last_update_dt": now()
                        }
                    )
            contents[str(wp.id)] = content
        return contents

        
