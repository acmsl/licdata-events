#!/usr/bin/env python3
"""
org/acmsl/licdata/events/clients/client_updated.py

This file defines the ClientUpdated class.

Copyright (C) 2024-today ACM S.L. Licdata-Events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from .base_client_event import BaseClientEvent
from pythoneda.shared import primary_key_attribute
from typing import List


class ClientUpdated(BaseClientEvent):
    """
    Represents events for updating Client instances.

    Class name: ClientUpdated

    Responsibilities:
        - Represent the event when a client has been updated.

    Collaborators:
        - None
    """

    def __init__(
        self,
        entityId: str,
        address: str,
        contact: str,
        phone: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new ClientUpdated instance.
        :param entityId: The id of the client.
        :type entityId: str
        :param address: The address.
        :type address: str
        :param contact: The contact information.
        :type contact: str
        :param phone: The phone.
        :type phone: str
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the events this one is response to,
        in case it's a reconstruction of an external event.
        :type reconstructedPreviousEventIds: str
        """
        super().__init__(
            entityId=entityId,
            address=address,
            contact=contact,
            phone=phone,
            previousEventIds=previousEventIds,
            reconstructedId=reconstructedId,
            reconstructedPreviousEventIds=reconstructedPreviousEventIds,
        )

    def apply_to(self, client: "Client"):
        """
        Applies this event to given client.
        :param client: The client.
        :type client: org.acmsl.licdata.Client
        """
        client.apply_updated(self)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
