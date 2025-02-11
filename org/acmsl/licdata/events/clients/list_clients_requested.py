#!/usr/bin/env python3
"""
org/acmsl/licdata/events/clients/list_clients_requested.py

This file defines the ListClientsRequested class.

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
from pythoneda.shared import attribute, Event
from typing import List, Optional


class ListClientsRequested(Event):
    """
    Represents events for creating new Client instances.

    Class name: ListClientsRequested

    Responsibilities:
        - Represent the event when a new Client is requested.

    Collaborators:
        - None
    """

    def __init__(
        self,
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
        previousEventIds: Optional[List[str]] = None,
        reconstructedId: Optional[str] = None,
        reconstructedPreviousEventIds: Optional[List[str]] = None,
    ):
        """
        Creates a new ListClientsRequested instance.
        :param offset: The offset.
        :type offset: Optional[int]
        :param limit: The maximum number of items to retrieve.
        :type limit: Optional[int]
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: Optional[List[str]]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: Optional[str]
        :param reconstructedPreviousEventIds: The id of the events this one is response to,
        in case it's a reconstruction of an external event.
        :type reconstructedPreviousEventIds: Optional[List[str]]
        """
        self._offset = offset
        self._limit = limit
        super().__init__(
            previousEventIds=previousEventIds,
            reconstructedId=reconstructedId,
            reconstructedPreviousEventIds=reconstructedPreviousEventIds,
        )

    @property
    @attribute
    def offset(self) -> Optional[int]:
        """
        Retrieves the offset.
        :return: Such value.
        :rtype: Optional[int]
        """
        return self._offset

    @property
    @attribute
    def limit(self) -> Optional[int]:
        """
        Retrieves the maximum number of items to retrieve.
        :return: Such value.
        :rtype: Optional[int]
        """
        return self._limit


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
