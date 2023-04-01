"""Define an interface to interact with a SQLite database.

The clas implements the DatabaseAdapter-Interface. For more information
look up the documentation of the Interface class.

Common Usage:
    data_base: DatabaseAdapter = SqliteAdapter()
    data_base.connect("data_base/in/memory")
"""

import pathlib
import sqlite3

from amo import data_objects


class SqliteAdapter:
    """Implements interactions for the SQLite database."""

    data_base_connection: sqlite3.Connection | None
    data_base: pathlib.Path

    def __init__(self, database: pathlib.Path) -> None:
        """Initialize sqlite database connection.

        Args:
            database: The path to the database in memory.
        """
        self.data_base = database
        self.data_base_connection = None

    def connect(self) -> bool:
        """Connect to a given database.

        Returns:
            bool: Sucessvalue of the operation
        """
        rv: bool = True
        try:
            self.data_base_connection = sqlite3.connect(self.data_base)
        except sqlite3.OperationalError:
            # TODO: log exception
            rv = False

        return rv

    def create(self, resouce_to_create: data_objects.Equipment) -> bool:
        """Create an object in the database.

        Args:
            resource_to_create: The object to create in the database.
        Returns:
            bool: Sucessvalue of the operation.
        """
        if not self.data_base_connection:
            return False

        cursor = self.data_base_connection.cursor()
        resouce_as_tuple = resouce_to_create.to_tuple()

        cursor.execute("""INSERT INTO weapon VALUES (?, ?, ?)""", resouce_as_tuple)

        return True

    def read(self) -> list[data_objects.Equipment]:
        """Read objects in the database.

        Returns:
            list[data_objects.Equipment]: The results of the querry.
        """
        ...

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
        ...

    def delete(self, resource_to_delete: data_objects.Equipment) -> bool:
        """Delete a given resource from the database.

        Args:
            resource_to_delete: The resource that will be deleted from the
                database.

        Returns:
            bool: Successvalue of the operation.
        """
        ...

    def disconnect(self) -> bool:
        """Disconnect from the database.

        Returns:
            bool: Sucessvalue of the operation
        """
        ...
