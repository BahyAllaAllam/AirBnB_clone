#!/usr/bin/python3
"""
Unit tests for the console using mock
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        self.assertTrue(self.cmd.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        self.assertTrue(self.cmd.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), '\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.cmd.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        self.cmd.onecmd("create BaseModel")
        self.assertTrue(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        self.cmd.onecmd("show BaseModel")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        self.cmd.onecmd("destroy BaseModel")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        self.cmd.onecmd("all")
        self.assertTrue(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        self.cmd.onecmd("update BaseModel 1234 name John")
        self.assertEqual(
            mock_stdout.getvalue().strip(), "** no instance found **")


if __name__ == '__main__':
    unittest.main()
