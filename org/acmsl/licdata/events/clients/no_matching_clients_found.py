#!/usr/bin/env python3
"""
org/acmsl/licdata/events/clients/no_matching_clients_found.py

This file defines the NoMatchingClientsFound class.

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
from pythoneda.shared import Event, primary_key_attribute
from typing import Dict, List


class NoMatchingClientsFound(Event):
    """
    Represents events when no matching clients are found.

    Class name: NoMatchingClientsFound

    Responsibilities:
        - Represent the event when no matching Clients are found.

    Collaborators:
        - None
    """

    def __init__(
        self,
        criteria: Dict,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new NoMatchingClientsFound instance.
        :param matchingClients: The matching clients.
        :type matchingClients: List[org.acmsl.licdata.Client]
        :param criteria: The filter criteria.
        :type criteria: Dict
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the events this one is response to,
        in case it's a reconstruction of an external event.
        :type reconstructedPreviousEventIds: str
        """
        self._criteria = criteria
        super().__init__(
            previousEventIds,
            reconstructedId,
            reconstructedPreviousEventIds,
        )

    @property
    @primary_key_attribute
    def criteria(self) -> Dict:
        """
        Retrieves the filter criteria.
        :return: Such criteria.
        :rtype: Dict
        """
        return self._criteria


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
