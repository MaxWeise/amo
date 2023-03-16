"""Definition of objects used in the database."""

import dataclasses
from abc import ABC, abstractmethod

import person


@dataclasses.dataclass
class Maintenance:
    """Represent a log-entry of any changes done to the equipment."""

    date: str
    maintainer: person.User
    contents: str


class Equipment(ABC):
    """Represent a piece of equipment storable by the programm.

    Attributes:
        id (readonly): The identifier of the equipment.
        maintenance_entries: A list of changes and reparations done to the
            equipment. Defaults to an empty list.
        owner: The current owner of the equipment. Defaults to a representation
            of the club itself.
    """
    _id: str
    maintenance_entries: list[Maintenance]
    owner: person.Person

    def __init__(self, identifier: str) -> None:
        self._id = identifier
        self.maintenance_entries = []
        self.owner = "TSG Reutlingen"

    @abstractmethod
    def add_maintenance(self, new_entry: Maintenance) -> None:
        pass

    @abstractmethod
    def change_owner(self, new_owner: person.Person) -> None:
        pass


@dataclasses.dataclass
class Weapon(Equipment):
    def add_maintenance(self, new_entry: Maintenance) -> None:
        pass

    def change_owner(self, new_owner: person.Person) -> None:
        pass
