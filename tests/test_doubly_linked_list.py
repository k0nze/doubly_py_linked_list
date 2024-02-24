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

    def test_remove_node(self):
        d = dll()
        self.assertEqual(len(d), 0)

        node_1 = d.add_node_behind_tail(1)
        node_2 = d.add_node_behind_tail(2)
        node_3 = d.add_node_behind_tail(3)
        d.add_node_behind_tail(4)
        d.add_node_behind_tail(5)
        node_6 = d.add_node_behind_tail(6)
        node_7 = d.add_node_behind_tail(7)
        self.assertEqual(len(d), 7)

        l = list(d)
        self.assertListEqual(l, [1, 2, 3, 4, 5, 6, 7])

        d.remove_node(node_3)
        self.assertEqual(len(d), 6)

        l = list(d)
        self.assertListEqual(l, [1, 2, 4, 5, 6, 7])

        d.remove_node(node_1)
        self.assertEqual(len(d), 5)
        self.assertEqual(d.head, node_2)

        l = list(d)
        self.assertListEqual(l, [2, 4, 5, 6, 7])

        d.remove_node(node_7)
        self.assertEqual(len(d), 4)
        self.assertEqual(d.tail, node_6)

        l = list(d)
        self.assertListEqual(l, [2, 4, 5, 6])
