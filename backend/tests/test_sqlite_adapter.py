"""Test the functionality of the SQLite database adapter."""

import os
import pathlib
import sqlite3
import unittest

from amo.sqlite_adapter import SqliteAdapter

# from typing import Any


class TestSqliteAdapter(unittest.TestCase):
    def setUp(self) -> None:
        """Create a database to run tests on."""
        self.path_to_test_db = pathlib.Path("./test_sqlite_db.db")

        # Setup an in-memory database
        # Connection must be closed so the tests can run properly
        self.test_database = sqlite3.connect(self.path_to_test_db)
        self.test_database.close()
        self.under_test = SqliteAdapter()

    def test_connect(self) -> None:
        """Test that the adapter sucessfully connects to the database."""
        actual: bool = self.under_test.connect(self.path_to_test_db)

        self.assertTrue(actual)
        self.assertIsNotNone(self.under_test.data_base_connection)

    def test_connect_E_dbDoesNotExist(self) -> None:
        """Test the correct behaviour when a given data base does not exist."""
        wrong_path = pathlib.Path("path/does/not/exist.db")
        actual: bool = self.under_test.connect(wrong_path)

        self.assertFalse(actual)

    @unittest.skip("not implemented")
    def test_create(self) -> None:
        """Test the creation of resources in the database."""
        pass

    @unittest.skip("not implemented")
    def test_read(self) -> None:
        """Test the read method."""
        pass

    @unittest.skip("not implemented")
    def test_update(self) -> None:
        """Test the functionality of the update method."""
        pass

    @unittest.skip("not implemented")
    def test_delete(self) -> None:
        """Test the correct deletion of resources in the database."""
        pass

    @unittest.skip("not implemented")
    def test_disconnect(self) -> None:
        """Test that the adapter sucessfully disconnects from the database."""
        pass

    def tearDown(self) -> None:
        os.remove(self.path_to_test_db)
