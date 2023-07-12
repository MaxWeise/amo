"""Test the functionality of the TinyDB database adapter."""

import pathlib
import unittest
from typing import Any

from amo import data_objects
from amo.data_objects import Equipment, Maintenance, Person, User
from amo.tinydb_adapter import TinyDBAdapter


class TestTinyDBAdapter(unittest.TestCase):
    """Test Suite for the TinyDBAdapter."""

    def setUp(self) -> None:
        """Create the test environment."""
        self.test_database_file = pathlib.Path("./test_database_file.json")
        self.under_test = TinyDBAdapter(self.test_database_file)
        self.test_objects: list[Equipment] = [
            data_objects.Weapon("#0L01"),
            data_objects.Weapon("#0L02"),
            data_objects.Weapon("#0L03"),
        ]

    def test_create(self) -> None:
        """Test the correct creation of resources in the database."""
        test_object: Equipment = data_objects.Weapon("#0L01")

        actual = self.under_test.create(test_object)
        actual_contents = self.under_test._database.all()

        self.assertTrue(actual)
        expected_db_contents = [test_object.to_dict()]
        self.assertEqual(actual_contents, expected_db_contents)

    def test_read(self) -> None:
        """Test the correct behavior when reading the database."""
        for entry in self.test_objects:
            self.under_test._database.insert(entry.to_dict())

        actual: list[dict[str, Any]] = self.under_test.read()

        expected: list[dict[str, Any]] = [
            entry.to_dict() for entry in self.test_objects
        ]
        self.assertEqual(actual, expected)

    def test_update_changeMaintenance(self) -> None:
        """Test the correct behavior when changing a resource."""
        for entry in self.test_objects:
            self.under_test._database.insert(entry.to_dict())

        test_user: User = data_objects.User(
            "user_name", "example@email.com", "Random Password"
        )
        test_maintenance_entry: Maintenance = data_objects.Maintenance(
            "01.01.2000", test_user, "Test Contents"
        )
        test_maintenance: list[Maintenance] = [test_maintenance_entry]

        test_object = self.test_objects[0]
        test_object_one = self.test_objects[1]
        ret: bool = self.under_test.update(
            test_object, new_maintenance_list=test_maintenance
        )
        actual_db_contents = self.under_test._database.all()

        self.assertTrue(ret)
        test_object.add_maintenance(test_maintenance_entry)
        self.assertEqual(test_object.to_dict(), actual_db_contents[0])
        self.assertEqual(test_object_one.to_dict(), actual_db_contents[1])

    def test_update_changeOwner(self) -> None:
        """Test the correct behavior when changing a resource."""
        for entry in self.test_objects:
            self.under_test._database.insert(entry.to_dict())

        test_owner: Person = data_objects.Person("user_name", "example@email.com")
        test_object = self.test_objects[0]
        test_object_one = self.test_objects[1]
        ret: bool = self.under_test.update(test_object, new_owner=test_owner)
        actual_db_contents = self.under_test._database.all()

        self.assertTrue(ret)
        test_object.change_owner(test_owner)
        self.assertEqual(test_object.to_dict(), actual_db_contents[0])
        self.assertEqual(test_object_one.to_dict(), actual_db_contents[1])

    def test_delete(self) -> None:
        """Test the correct behavior when deleting from the database."""
        for entry in self.test_objects:
            self.under_test._database.insert(entry.to_dict())
        test_object_one = self.test_objects[1]

        ret: bool = self.under_test.delete(test_object_one.identifier)

        self.assertTrue(ret)
        actual_db_contents = self.under_test._database.all()
        expected_db_contents = [
            self.test_objects[0].to_dict(),
            self.test_objects[2].to_dict(),
        ]
        self.assertEqual(actual_db_contents, expected_db_contents)

    def tearDown(self) -> None:
        """Tear down the test environment."""
        # Ignore FileNotFoundExeption
        self.test_database_file.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
