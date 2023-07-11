"""Test the functionality of the TinyDB database adapter."""

import pathlib
import unittest

import tinydb
from amo import data_objects
from amo.data_objects import Equipment
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

    @unittest.skip("Not Implemented")
    def test_read(self) -> None:
        """Test the correct behavior when reading the database."""
        pass

    @unittest.skip("Not Implemented")
    def test_update(self) -> None:
        """Test the correct behavior when changing a resource."""
        pass

    @unittest.skip("Not Implemented")
    def test_delete(self) -> None:
        """Test the correct behavior when deleting from the database."""
        pass

    @unittest.skip("Not Implemented")
    def test_disconnect(self) -> None:
        """Test the correct disconnection behavior."""
        pass

    def tearDown(self) -> None:
        """Tear down the test environment."""
        # Ignore FileNotFoundExeption
        self.test_database_file.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
