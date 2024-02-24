import unittest

from doubly_py_linked_list import DoublyLinkedList as dll


class TestDoublyLinkedList(unittest.TestCase):
    def test_add_in_front_of_head(self):
        d = dll()

        self.assertEqual(len(d), 0)

        d.add_node_in_front_of_head(1)
        self.assertEqual(len(d), 1)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 1)

        d.add_node_in_front_of_head(2)
        self.assertEqual(len(d), 2)
        self.assertEqual(d.head.value, 2)
        self.assertEqual(d.tail.value, 1)

        d.add_node_in_front_of_head(3)
        self.assertEqual(len(d), 3)
        self.assertEqual(d.head.value, 3)
        self.assertEqual(d.tail.value, 1)

    def test_add_behind_tail(self):
        d = dll()
        self.assertEqual(len(d), 0)

        d.add_node_behind_tail(1)
        self.assertEqual(len(d), 1)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 1)

        d.add_node_behind_tail(2)
        self.assertEqual(len(d), 2)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 2)

        d.add_node_behind_tail(3)
        self.assertEqual(len(d), 3)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 3)
