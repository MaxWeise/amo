"""Test the functionality of the SQLite database adapter."""

import os
import pathlib
import sqlite3
import unittest

from amo import data_objects
from amo.sqlite_adapter import SqliteAdapter


class TestSqliteAdapter(unittest.TestCase):
    def setUp(self) -> None:
        """Create a database to run tests on."""
        self.test_db = pathlib.Path("./test_sqlite_db.db")
        self.under_test = SqliteAdapter(self.test_db)
        self.test_resource: data_objects.Equipment = data_objects.Weapon("#5L01")

    def _setup_test_connection(self, data_base: pathlib.Path):
        con = sqlite3.connect(data_base)
        cur = con.cursor()
        return con, cur

    def test_connect(self) -> None:
        """Test that the adapter sucessfully connects to the database."""
        actual: bool = self.under_test.connect()

        self.assertTrue(actual)
        self.assertIsNotNone(self.under_test.data_base_connection)

    def test_connect_E_dbDoesNotExist(self) -> None:
        """Test the correct behaviour when a given data base does not exist."""
        wrong_path = pathlib.Path("path/does/not/exist.db")
        self.under_test.data_base = wrong_path
        actual: bool = self.under_test.connect()

        self.assertFalse(actual)

    @unittest.skip("Provide propper db scheme to test the database correctly")
    def test_create(self) -> None:
        """Test the creation of resources in the database."""
        # setup table
        conn, cursor = self._setup_test_connection(self.test_db)
        cursor.execute(
            """CREATE TABLE weapon(identifier TEXT, maintenance, TEXT owner TEXT)"""
        )

        # Run the test
        self.under_test.data_base_connection = sqlite3.connect(self.test_db)
        actual: bool = self.under_test.create(self.test_resource)

        # Retrieve information
        cursor.execute("""SELECT * FROM weapon""")
        result = cursor.fetchall()
        conn.close()

        # assert statements
        self.assertTrue(actual)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.test_resource)

    def test_create_E_noDbConnection(self) -> None:
        """Test the correct behaviour when no connection was established."""
        actual: bool = self.under_test.create(self.test_resource)

        self.assertFalse(actual)

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
        try:
            os.remove(self.test_db)
        except FileNotFoundError:
            print("Test did not create database. Moving on.")
