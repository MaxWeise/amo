"""Define classes that represent humans.

This file contains the definition of classes used to describe humans. To define
an object that holds general information about a human being, the person class
is used. A human described with a 'person' object does not necessarily
interact with the system. Users on the other hand are persons that interact
with the system.
"""

import dataclasses


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
