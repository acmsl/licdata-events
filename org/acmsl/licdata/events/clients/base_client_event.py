#!/usr/bin/env python3
"""
org/acmsl/licdata/events/clients/new_client_requested.py

This file defines the BaseClientEvent class.

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
import abc
from pythoneda.shared import attribute, Event
from typing import List, Optional


class BaseClientEvent(Event, abc.ABC):
    """
    Base class for client-related events.

    Class name: BaseClientEvent

    Responsibilities:
        - Common data and logic for client events.

    Collaborators:
        - None
    """

    def __init__(
        self,
        entityId: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None,
        contact: Optional[str] = None,
        phone: Optional[str] = None,
        previousEventIds: Optional[List[str]] = None,
        reconstructedId: Optional[str] = None,
        reconstructedPreviousEventIds: Optional[List[str]] = None,
    ):
        """
        Creates a new BaseClientEvent instance.
        :param entityId: The id of the client.
        :type entityId: Optional[str]
        :param email: The email.
        :type email: Optional[str]
        :param address: The address.
        :type address: Optional[str]
        :param contact: The contact information.
        :type contact: Optional[str]
        :param phone: The phone.
        :type phone: Optional[str]
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: Optional[List[str]]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: Optional[str]
        :param reconstructedPreviousEventIds: The id of the events this one is response to,
        in case it's a reconstruction of an external event.
        :type reconstructedPreviousEventIds: Optional[List[str]]
        """
        self._entity_id = entityId
        self._email = email
        self._address = address
        self._contact = contact
        self._phone = phone
        super().__init__(
            previousEventIds, reconstructedId, reconstructedPreviousEventIds
        )

    @property
    @attribute
    def entity_id(self) -> Optional[str]:
        """
        Retrieves the entity id.
        :return: Such id.
        :rtype: str
        """
        return self._entity_id

    @property
    @attribute
    def email(self) -> Optional[str]:
        """
        Retrieves the email.
        :return: Such email.
        :rtype: str
        """
        return self._email

    @property
    @attribute
    def address(self) -> Optional[str]:
        """
        Retrieves the address.
        :return: Such address.
        :rtype: str
        """
        return self._address

    @property
    @attribute
    def contact(self) -> Optional[str]:
        """
        Retrieves the contact.
        :return: Such contact.
        :rtype: str
        """
        return self._contact

    @property
    @attribute
    def phone(self) -> Optional[str]:
        """
        Retrieves the phone.
        :return: Such phone.
        :rtype: str
        """
        return self._phone


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
