#!/usr/bin/env python3
"""
org/acmsl/licdata/events/clients/find_client_by_id_requested.py

This file defines the FindClientByIdRequested class.

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
from pythoneda.shared import Event
from typing import List, Optional


class FindClientByIdRequested(Event):
    """
    Represents events for creating new Client instances.

    Class name: FindClientByIdRequested

    Responsibilities:
        - Represent the event when a new Client is requested.

    Collaborators:
        - None
    """

    def __init__(
        self,
        entityId: str,
        previousEventIds: Optional[List[str]] = None,
        reconstructedId: Optional[str] = None,
        reconstructedPreviousEventIds: Optional[List[str]] = None,
    ):
        """
        Creates a new FindClientByIdRequested instance.
        :param email: The email of the client.
        :type email: str
        """
        self._entity_id = entityId
        super().__init__(
            previousEventIds=previousEventIds,
            reconstructedId=reconstructedId,
            reconstructedPreviousEventIds=reconstructedPreviousEventIds,
        )

    @property
    def entity_id(self) -> str:
        """
        Retrievves the id of the entity.
        :return: Such value.
        :rtype: str
        """
        return self._entity_id


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
