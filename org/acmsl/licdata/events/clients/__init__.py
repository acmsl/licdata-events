# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/clients/__init__.py

This file ensures org.acmsl.licdata.events.clients is a namespace.

Copyright (C) 2024-today acmsl's licdata-events

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .base_client_event import BaseClientEvent
from .invalid_new_client_request import InvalidNewClientRequest
from .client_already_exists import ClientAlreadyExists
from .new_client_created import NewClientCreated
from .new_client_requested import NewClientRequested
from .list_clients_requested import ListClientsRequested
from .matching_client_found import MatchingClientFound
from .matching_clients_found import MatchingClientsFound
from .no_matching_clients_found import NoMatchingClientsFound
from .invalid_list_clients_request import InvalidListClientsRequest
from .delete_client_requested import DeleteClientRequested
from .client_deleted import ClientDeleted
from .invalid_delete_client_request import InvalidDeleteClientRequest
from .find_client_by_id_requested import FindClientByIdRequested
from .invalid_find_client_by_id_request import InvalidFindClientByIdRequest

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
