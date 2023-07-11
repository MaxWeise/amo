"""Definition of objects used in the database."""

import dataclasses
from abc import ABC, abstractmethod
from typing import Any


@dataclasses.dataclass
class Person:
    """Represent information about a human being in the system.

    Attributes:
        first_name: The first name of the person.
        last_name: The last name of the person.
    """

    first_name: str
    last_name: str


@dataclasses.dataclass
class User(Person):
    """Represent a person that interacts with the system.

    Attributes:
        [first_name]
        [last_name]
        user_name: The user name in the system. Serves as a unique identifier.
        email: The email of the user.
        password: The password of the user.
    """

    user_name: str = ""
    email: str = ""
    password: str = ""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        user_name: str = "",
        email: str = "",
        password: str = "",
    ) -> None:
        """Initialize a user object.

        Arguments:
            first_name: The first name of the user
            last_name: The last name of the user
            user_name: Unique identifier for the user
            email: Email adress of the user
            password: The password of the user
        """
        self.user_name = user_name
        self.email = email
        self.password = password
        super().__init__(first_name, last_name)


@dataclasses.dataclass
class Maintenance:
    """Represent a log-entry of any changes done to the equipment."""

    date: str
    maintainer: User
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

    _identifier: str
    maintenance_entries: list[Maintenance]
    owner: Person

    def __init__(self, identifier: str) -> None:
        """Initialize an object of type equipment.

        This is a default implementation of the constructor for all subclasses
        to use.  The constructor initializes an empty list of maintenance
        entries and sets the owner of the equipment to the default owner.

        Arguments:
            identifier: The id of a piece of equipment.
        """
        self._identifier = identifier
        self.maintenance_entries = []
        self.owner = Person("TSG Reutlingen", "Fencing Department")

    @property
    def identifier(self) -> str:
        """The id string of the equipment."""
        return self._identifier

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """Return a dictionary representation of the calling object.

        Returns:
            The object represented as a dictionary.
        """
        pass

    @abstractmethod
    def to_tuple(self) -> tuple[str, list[Maintenance], Person]:
        """Return the object as a tuple.

        Returns:
            The object represented as a tuple.
        """
        pass

    @abstractmethod
    def add_maintenance(self, new_entry: Maintenance) -> None:
        """Add a new entry to the list of maintenances.

        Args:
            new_entry: The entry to be added to the list.
        """
        pass

    @abstractmethod
    def change_owner(self, new_owner: Person) -> None:
        """Change the owner of the quipment.

        This method only modifies the calling object.

        Args:
            new_owner: The new (current) owner of the equipment.
        """
        pass


@dataclasses.dataclass
class Weapon(Equipment):
    """Representation of a weapon object in the system.

    Attributtes:
        [See base class]
    """

    def __init__(self, identifier: str) -> None:
        """Ininitialize weapon object by calling the super constructor.

        [See base class for more information]

        Args:
            identifier: The unique identifier for the weapon.
        """
        super().__init__(identifier)

    def to_dict(self) -> dict[str, Any]:
        """Return a dictionary representation of the calling object.

        Returns:
            The object represented as a dictionary.
        """
        return {
            "identifier": self.identifier,
            "maintenance": self.maintenance_entries,
            "owner": dataclasses.asdict(self.owner),
        }

    def to_tuple(self) -> tuple[str, list[Maintenance], Person]:
        """Return the object as a tuple.

        Returns:
            The object represented as a tuple.
        """
        return (self.identifier, self.maintenance_entries, self.owner)

    def add_maintenance(self, new_entry: Maintenance) -> None:
        """Add a new entry to the list of maintenances.

        Args:
            new_entry: The entry to be added to the list.
        """
        self.maintenance_entries.append(new_entry)

    def change_owner(self, new_owner: Person) -> None:
        """Change the owner of the quipment.

        [See base class]

        Args:
            new_owner: The new (current) owner of the equipment.
        """
        self.owner = new_owner
