from datetime import datetime, timedelta
from typing import Dict
import requests

from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
from django.conf import settings

from dalec.proxy import Proxy

from pyopenproject.openproject import OpenProject
from pyopenproject.model.project import Project
from pyopenproject.business.util.filter import Filter

client = OpenProject(
    url=settings.DALEC_OPENPROJECT_BASE_URL,
    api_key=settings.DALEC_OPENPROJECT_API_TOKEN,
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

        raise ValueError(
            f"Invalid content_type {content_type}. Accepted: work_package."
        )

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

        project_service = client.get_project_service()

        project_identifier = channel_object
        project = project_service.find_all(
            [Filter("name_and_identifier", "=", [project_identifier])]
        )
        if not project:
            raise ValueError(f"The project {project_identifier} is not found.")

        # project is a list of 1 element
        project = project[0]

        # eventually fetch work packages
        work_packages = project_service.find_work_packages(project)

        # prepare contents
        contents = {}

        project_attrs = project.__dict__
        project_attrs.update(
            {
                "project_url": f"{settings.DALEC_OPENPROJECT_BASE_URL}/projects/{project.id}"
            }
        )

        for wp in work_packages:
            # remove _links attribute (or similar)
            content = {
                attr: getattr(wp, attr) for attr in dir(wp) if not attr.startswith("_")
            }
            content["dueDate"] = datetime.strptime(content["dueDate"], "%Y-%m-%d")
            content.update(
                {
                    "work_package_url": f"{settings.DALEC_OPENPROJECT_BASE_URL}/work_packages/{wp.id}",
                    "assignee": wp._links["assignee"].get("title", None)
                }
            )

            # project attributes
            content.update(
                {
                    "project": project_attrs,
                }
            )

            # dalec needed attribues
            content.update(
                {
                    "id": str(wp.id),
                    "creation_dt": wp.createdAt,
                    "last_update_dt": now(),
                }
            )

            contents[str(wp.id)] = content
        return contents
