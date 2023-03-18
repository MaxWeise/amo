"""Test suite for methods and properties of the data_objects module."""

import unittest

from amo import data_objects, person


class TestWeapon(unittest.TestCase):
    """Test the correct behaviour of the weapon class."""

    _test_id: str = "5L01"
    _test_user: person.User | None = None

    def setUp(self) -> None:
        """Setup test environment."""
        self.under_test = data_objects.Weapon(self._test_id)
        self._test_user = self._create_test_user()
        self._test_maintenance_entry = data_objects.Maintenance(
            "01.01.2000", self._test_user, "This is a testentry for debugging."
        )

    def _create_test_user(self) -> person.User:
        return person.User(
            "Max",
            "Mustermann",
            user_name="maxmustermann",
            email="max.mustermann@examplemail.com",
            password="12345",  # noqa
        )

    def test_addMaintenance(self) -> None:
        """Test the correct behaviour of the method."""
        self.under_test.add_maintenance(self._test_maintenance_entry)

        self.assertEqual(len(self.under_test.maintenance_entries), 1)

    def test_changeOwner(self) -> None:
        """Test that the owner of the weapon is correctly changed."""
        test_owner = person.Person("Bob", "Bobington")
        self.under_test.change_owner(test_owner)

        self.assertNotEqual(self.under_test.owner, self._test_user)
        self.assertEqual(self.under_test.owner, test_owner)

    def tearDown(self) -> None:
        """Destroy test environment."""
        pass
