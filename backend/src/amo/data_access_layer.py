"""Define functions to manipulate data inbetween database and api layer."""

import pathlib
from pathlib import Path
from typing import Any

from amo import data_base_connector, data_objects, tinydb_adapter

# Type definition
data_object = dict[str, Any]

# Constant definitions
DATABASE_PATH: Path = pathlib.Path("database.json")
DATABASE: data_base_connector.DatabaseAdapter = tinydb_adapter.TinyDBAdapter(
    DATABASE_PATH
)


def get_weapons() -> list[data_object]:
    """Get a list of all weapon objects in the database.

    Returns:
        list[data_object]: The list of weapons from the database.

    """
    return DATABASE.read()


def update_weapon(
    weapon_to_update: data_objects.Equipment, new_version: data_objects.Equipment
) -> bool:
    """Replace weapon object with an updated version.

    Args:
        weapon_to_update (Equipment): The object to update.
        new_version: The updated version of weapon_to_update.

    Returns:
        bool: Sucessvalue of the function.
    """
    return DATABASE.update(
        weapon_to_update, new_version.maintenance_entries, new_version.owner
    )


def insert_weapon(new_weapon: data_objects.Equipment) -> bool:
    """Insert a new weapon object into the database.

    Args:
        _o (Equipment): The object to insert.

    Returns:
        bool: Sucessvalue of the function.
    """
    return DATABASE.create(new_weapon)


def delete_weapon(weapon_to_delete: data_objects.Equipment) -> bool:
    """Remove a weapon from the database.

    Args:
        _o (Equipment): The object to delete.

    Returns:
        bool: Sucessvalue of the function.
    """
    return DATABASE.delete(weapon_to_delete._identifier)
