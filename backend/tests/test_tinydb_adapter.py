"""Test the functionality of the TinyDB database adapter."""

import pathlib
import unittest

from amo.tinydb_adapter import TinyDBAdapter


class TestTinyDBAdapter(unittest.TestCase):
    """Test Suite for the TinyDBAdapter."""

    def setUp(self) -> None:
        """Setup the test environment."""
        pass

    @unittest.skip("Not Implemented")
    def test_connect(self) -> None:
        """Test the correct connection to a database."""
        test_path = pathlib.Path("./test_database.json")
        under_test = TinyDBAdapter(test_path)

        rv: bool = under_test.connect()

        self.assertTrue(rv)
        self.assertIsNotNone(under_test._database)

    @unittest.skip("Not Implemented")
    def test_create(self) -> None:
        """Test the correct creation of resources in the database."""
        pass

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
        pass


if __name__ == "__main__":
    unittest.main()
