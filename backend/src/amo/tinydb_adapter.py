"""Provides an interface to the TinyDB nosql database.

According to the documentation, the database is a wrapper for the json library
and provides an interface to store json / dictionary objects in database style
in memory.
"""

import pathlib
from typing import Any

import tinydb
from tinydb.table import Table

from amo import data_objects


class TinyDBAdapter:
    """Provides an interface to the tinyDB nosql Database.

    Attributes:
        _db_connection_path: The path to the in memory database.
    """

    def __init__(self, db_connection_path: pathlib.Path) -> None:
        """Initialize a database adapter.

        Expects the path to a database. If the file does not exist,
        it will be created.

        Args:
            db_connection_path: The path to the database.
        """
        self._db_connection_path: pathlib.Path | None = db_connection_path
        self._database: Table = tinydb.TinyDB(self._db_connection_path)

    def create(self, resouce_to_create: data_objects.Equipment) -> bool:
        """Create an object in the database.

        Args:
            resource_to_create: The object to create in the database.
        Returns:
            bool: Sucessvalue of the operation.
        """
        identifier = self._database.insert(resouce_to_create.to_dict())

        return bool(identifier)

    def read(self) -> list[dict[str, Any]]:
        """Read objects in the database.

        Returns:
            list[data_objects.Equipment]: The result of the querry.
        """
        data_base_contents: list[dict[str, Any]] = self._database.all()

        return data_base_contents

    def update(
        self,
        resouce_to_update: data_objects.Equipment,
        new_resource: data_objects.Equipment,
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

    def delete(self, resource_to_delete: data_objects.Equipment) -> bool:
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

    def disconnect(self) -> bool:
        """Disconnect from the database.

        Returns:
            bool: Sucessvalue of the operation
        """
        raise NotImplementedError(
            f"The method is not implemented for the type {type(self)}"
        )
