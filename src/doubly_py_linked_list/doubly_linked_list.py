from typing import Any, Optional

__version__ = "1.0.0"


class DoublyLinkedListNode:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[DoublyLinkedListNode] = None
        self.prev: Optional[DoublyLinkedListNode] = None

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.__repr__()


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None
        self.length: int = 0

    def insert_head(self, value: Any) -> DoublyLinkedListNode:
        new_node = DoublyLinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return new_node

    def insert_tail(self, value) -> DoublyLinkedListNode:
        new_node = DoublyLinkedListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node

    def remove(self, node: DoublyLinkedListNode) -> None:
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.next.prev = None
        elif node is self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            next_node = node.next
            prev_node = node.prev
            next_node.prev = prev_node
            prev_node.next = next_node

        self.length -= 1
        node.prev = None
        node.next = None

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> "DoublyLinkedList":
        self.current_iter_node = self.head
        return self

    def __next__(self) -> DoublyLinkedListNode:
        if self.current_iter_node is not None:
            return_node = self.current_iter_node
            self.current_iter_node = self.current_iter_node.next
            return return_node.value
        raise StopIteration

    def __repr__(self) -> str:
        node_values = []

        if self.head is None:
            return "empty DoublyLinkedList"

        current_node = self.head
        node_values.append(str(current_node))

        while current_node.next != None:
            current_node = current_node.next
            node_values.append(str(current_node))

        print(node_values)

        return " <-> ".join(node_values)
