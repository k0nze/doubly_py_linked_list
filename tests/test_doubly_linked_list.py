import unittest

from doubly_py_linked_list import DoublyLinkedList as dll


class TestDoublyLinkedList(unittest.TestCase):
    def test_add_in_front_of_head(self):
        d = dll()

        self.assertEqual(len(d), 0)
