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

    def test_create(self) -> None:
        """Test the correct creation of resources in the database."""
        # Setup Code
        test_object: Equipment = data_objects.Weapon("#0L01")

        # Run Test
        actual = self.under_test.create(test_object)

        # Assert Statements
        self.assertTrue(actual)
        actual_contents = self.under_test._database.all()
        self.assertEqual([test_object.to_dict()], actual_contents)

    def test_read(self) -> None:
        """Test the correct behavior when reading the database."""
        # Setup Code
        test_object: Equipment = data_objects.Weapon("#0L01")
        test_object_one: Equipment = data_objects.Weapon("#0L02")
        test_object_two: Equipment = data_objects.Weapon("#0L03")
        entry_list: list[Equipment] = [test_object, test_object_one, test_object_two]
        for entry in entry_list:
            self.under_test._database.insert(entry.to_dict())

        # Run Test
        actual: list[dict[str, Any]] = self.under_test.read()

        # Assert Statements
        expected: list[dict[str, Any]] = [entry.to_dict() for entry in entry_list]
        self.assertEqual(actual, expected)

    def test_update_changeMaintenance(self) -> None:
        """Test the correct behavior when changing a resource."""
        # Setup Code
        test_object: Equipment = data_objects.Weapon("#0L01")
        self.under_test._database.insert(test_object.to_dict())
        test_object_one: Equipment = data_objects.Weapon("#0L02")
        self.under_test._database.insert(test_object_one.to_dict())

        test_user: User = data_objects.User(
            "user_name", "example@email.com", "Random Password"
        )
        test_maintenance_entry: Maintenance = data_objects.Maintenance(
            "01.01.2000", test_user, "Test Contents"
        )
        test_maintenance: list[Maintenance] = [test_maintenance_entry]

        # Run Test
        ret: bool = self.under_test.update(
            test_object, new_maintenance_list=test_maintenance
        )
        actual_db_contents = self.under_test._database.all()

        # Assert Statements
        self.assertTrue(ret)
        test_object.add_maintenance(test_maintenance_entry)
        self.assertEqual(test_object.to_dict(), actual_db_contents[0])
        self.assertEqual(test_object_one.to_dict(), actual_db_contents[1])

    def test_update_changeOwner(self) -> None:
        """Test the correct behavior when changing a resource."""
        # Setup Code
        test_object: Equipment = data_objects.Weapon("#0L01")
        self.under_test._database.insert(test_object.to_dict())
        test_object_one: Equipment = data_objects.Weapon("#0L02")
        self.under_test._database.insert(test_object_one.to_dict())

        test_owner: Person = data_objects.Person("user_name", "example@email.com")

        # Run Test
        ret: bool = self.under_test.update(test_object, new_owner=test_owner)
        actual_db_contents = self.under_test._database.all()

        # Assert Statements
        self.assertTrue(ret)
        test_object.change_owner(test_owner)
        self.assertEqual(test_object.to_dict(), actual_db_contents[0])
        self.assertEqual(test_object_one.to_dict(), actual_db_contents[1])

    def test_delete(self) -> None:
        """Test the correct behavior when deleting from the database."""
        # Setup Code
        test_object: Equipment = data_objects.Weapon("#0L01")
        self.under_test._database.insert(test_object.to_dict())
        test_object_one: Equipment = data_objects.Weapon("#0L02")
        self.under_test._database.insert(test_object_one.to_dict())
        test_object_two: Equipment = data_objects.Weapon("#0L03")
        self.under_test._database.insert(test_object_two.to_dict())

        # Run Test
        ret: bool = self.under_test.delete(test_object_one.identifier)

        # Assert Statemens
        self.assertTrue(ret)

        actual_db_contents = self.under_test._database.all()
        expected_db_contents = [test_object.to_dict(), test_object_two.to_dict()]
        self.assertEqual(actual_db_contents, expected_db_contents)

    def tearDown(self) -> None:
        """Tear down the test environment."""
        # Ignore FileNotFoundExeption
        self.test_database_file.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
