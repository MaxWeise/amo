"""Define classes that represent humans.

This file contains the definition of classes used to describe humans. To define
an object that holds general information about a human being, the person class
is used. A human described with a 'person' object does not necessarily
interact with the system. Users on the other hand are persons that interact
with the system.
"""

import dataclasses

import data_objects


@dataclasses.dataclass
class Person:
    """Represent information about a human being in the system.

    Attributes:
        first_name: The first name of the person.
        last_name: The last name of the person.
        owned_equipment: A list of equipment owned by the person. Defaults to
            the empty list.
    """

    first_name: str
    last_name: str
    owned_equipment: list[data_objects.Equipment] = dataclasses.field(
        default_factory=list
    )


@dataclasses.dataclass
class User(Person):
    """Represent a person that interacts with the system.

    Attributes:
        [first_name]
        [last_name]
        [owned_equipment]
        user_name: The user name in the system. Serves as a unique identifier.
        email: The email of the user.
        password: The password of the user.
    """

    user_name: str
    email: str
    password: str
