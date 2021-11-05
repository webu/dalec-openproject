from datetime import timedelta
from typing import Dict
import requests

from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
from django.conf import settings

from dalec.proxy import Proxy

from pyopenproject.openproject import OpenProject

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
        if content_type == "event":
            return self._fetch_event(nb, channel, channel_object)

        raise ValueError(f"Invalid content_type {content_type}. Accepted: event." )

    def _fetch_event(self, nb, channel=None, channel_object=None):
        """
        Get latest event from calendar
        """
        options = {
                "per_page": nb,
                }

        # TODO
