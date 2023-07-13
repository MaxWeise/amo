"""Define the database adapter interface in this file.

This file contains the database connector interface. It defines the basic set
of operations needed to acess a database and manipulate data. The Interface
relies on the pathlib library to represent paths to the in-memory databases.
"""

import typing
from typing import Any

from amo import data_objects


class DatabaseAdapter(typing.Protocol):
    """Define a unified interface for database services."""

    def create(self, resouce_to_create: data_objects.Equipment) -> bool:
        """Create an object in the database.

        Args:
            resource_to_create: The object to create in the database.
        Returns:
            bool: Sucessvalue of the operation.
        """
        raise NotImplementedError(
            f"The method is not implemented for the type {type(self)}"
        )

    def read(self) -> list[dict[str, Any]]:
        """Read objects in the database.

        Returns:
            list[data_objects.Equipment]: The result of the querry.
        """
        raise NotImplementedError(
            f"The method is not implemented for the type {type(self)}"
        )

    def update(
        self,
        resouce_to_update: data_objects.Equipment,
        new_maintenance_list: None | list[data_objects.Maintenance] = None,
        new_owner: None | data_objects.Person = None,
    ) -> bool:
        """Update a given resource with the values of another resource.

        Args:
            resource_to_update: The resource to be updated in the database.
            new_resource: An object holding the new values for the resource.

        Returns:
            bool: Sucessvalue of the operation.
        """
        raise NotImplementedError(
            f"The method is not implemented for the type {type(self)}"
        )

    def delete(self, id_to_delete: str) -> bool:
        """Delete a given resource from the database.

        Args:
            resource_to_delete: The resource that will be deleted from the
                database.

        Returns:
            bool: Successvalue of the operation.
        """
        raise NotImplementedError(
            f"The method is not implemented for the type {type(self)}"
        )
