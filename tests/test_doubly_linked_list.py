import unittest

from doubly_py_linked_list import DoublyLinkedList as dll


class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_head(self):
        d = dll()

        self.assertEqual(len(d), 0)

        d.insert_head(1)
        self.assertEqual(len(d), 1)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 1)

        d.insert_head(2)
        self.assertEqual(len(d), 2)
        self.assertEqual(d.head.value, 2)
        self.assertEqual(d.tail.value, 1)

        d.insert_head(3)
        self.assertEqual(len(d), 3)
        self.assertEqual(d.head.value, 3)
        self.assertEqual(d.tail.value, 1)

    def test_add_behind_tail(self):
        d = dll()
        self.assertEqual(len(d), 0)

        d.insert_tail(1)
        self.assertEqual(len(d), 1)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 1)

        d.insert_tail(2)
        self.assertEqual(len(d), 2)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 2)

        d.insert_tail(3)
        self.assertEqual(len(d), 3)
        self.assertEqual(d.head.value, 1)
        self.assertEqual(d.tail.value, 3)

    def test_remove_node(self):
        d = dll()
        self.assertEqual(len(d), 0)

        node_1 = d.insert_tail(1)
        node_2 = d.insert_tail(2)
        node_3 = d.insert_tail(3)
        d.insert_tail(4)
        d.insert_tail(5)
        node_6 = d.insert_tail(6)
        node_7 = d.insert_tail(7)
        self.assertEqual(len(d), 7)

        l = list(d)
        self.assertListEqual(l, [1, 2, 3, 4, 5, 6, 7])

        d.remove(node_3)
        self.assertEqual(len(d), 6)

        l = list(d)
        self.assertListEqual(l, [1, 2, 4, 5, 6, 7])

        d.remove(node_1)
        self.assertEqual(len(d), 5)
        self.assertEqual(d.head, node_2)

        l = list(d)
        self.assertListEqual(l, [2, 4, 5, 6, 7])

        d.remove(node_7)
        self.assertEqual(len(d), 4)
        self.assertEqual(d.tail, node_6)

        l = list(d)
        self.assertListEqual(l, [2, 4, 5, 6])

    def test_move_to_head(self):
        d = dll()

        d.insert_tail(1)
        d.insert_tail(2)
        node_3 = d.insert_tail(3)
        d.insert_tail(4)
        node_5 = d.insert_tail(5)
        node_6 = d.insert_tail(6)

        self.assertEqual(len(d), 6)

        d.move_to_head(node_3)
        self.assertEqual(d.head.value, 3)
        self.assertEqual(d.head, node_3)

        l = list(d)
        self.assertListEqual(l, [3, 1, 2, 4, 5, 6])

        d.move_to_head(node_6)
        self.assertEqual(d.head.value, 6)
        self.assertEqual(d.head, node_6)
        self.assertEqual(d.tail.value, 5)
        self.assertEqual(d.tail, node_5)

        l = list(d)
        self.assertListEqual(l, [6, 3, 1, 2, 4, 5])

        d.move_to_head(node_6)
        self.assertEqual(d.head.value, 6)
        self.assertEqual(d.head, node_6)

        l = list(d)
        self.assertListEqual(l, [6, 3, 1, 2, 4, 5])

    def test_move_to_tail(self):
        d = dll()

        node_1 = d.insert_tail(1)
        node_2 = d.insert_tail(2)
        node_3 = d.insert_tail(3)
        d.insert_tail(4)
        d.insert_tail(5)
        d.insert_tail(6)

        self.assertEqual(len(d), 6)

        d.move_to_tail(node_3)
        self.assertEqual(d.tail.value, 3)
        self.assertEqual(d.tail, node_3)

        l = list(d)
        self.assertListEqual(l, [1, 2, 4, 5, 6, 3])

        d.move_to_tail(node_1)
        self.assertEqual(d.tail.value, 1)
        self.assertEqual(d.tail, node_1)
        self.assertEqual(d.head.value, 2)
        self.assertEqual(d.head, node_2)

        l = list(d)
        self.assertListEqual(l, [2, 4, 5, 6, 3, 1])

        d.move_to_tail(node_1)
        self.assertEqual(d.tail.value, 1)
        self.assertEqual(d.tail, node_1)

        l = list(d)
        self.assertListEqual(l, [2, 4, 5, 6, 3, 1])

    def test_init_with_values(self):
        d = dll([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(len(d), 7)

        l = list(d)
        self.assertListEqual(l, [1, 2, 3, 4, 5, 6, 7])

    def test_nodes(self):
        d = dll()

        node_1 = d.insert_tail(1)
        node_2 = d.insert_tail(2)
        node_3 = d.insert_tail(3)
        node_4 = d.insert_tail(4)

        nodes = d.nodes()
        self.assertListEqual(nodes, [node_1, node_2, node_3, node_4])
