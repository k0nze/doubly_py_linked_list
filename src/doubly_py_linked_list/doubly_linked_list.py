from typing import List, Any, Optional

__version__ = "1.0.0"


class DoublyLinkedListNode:
    """
    A node in a doubly linked list

    Attributes
    ----------
    value: Any
        The value of the node

    next: Optional[DoublyLinkedListNode]
        The next node in the doubly linked list

    prev: Optional[DoublyLinkedListNode]
        The previous node in the doubly linked list
    """

    def __init__(self, value: Any):
        """
        Create a new node in a doubly linked list
        """
        self.value = value
        self.next: Optional[DoublyLinkedListNode] = None
        self.prev: Optional[DoublyLinkedListNode] = None

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.__repr__()


class DoublyLinkedList:
    """
    A doubly linked list

    Attributes
    ----------
    head: Optional[DoublyLinkedListNode]
        The head of the doubly linked list

    tail: Optional[DoublyLinkedListNode]
        The tail of the doubly linked list

    length: int
        The number of nodes in the doubly linked list
    """

    def __init__(self, values: Optional[List[Any]] = None):
        """
        Create a new doubly linked list

        Parameters
        ----------
        values: List[Any]
            A list of values to initialize the doubly linked list with
        """
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None
        self.length: int = 0

        if values is not None:
            for value in values:
                self.insert_tail(value)

    def insert_head(self, value: Any) -> DoublyLinkedListNode:
        """
        Insert a value at the head of the doubly linked list

        Parameters
        ----------
        value: Any
            The value to insert

        Returns:
        --------
        DoublyLinkedListNode
            The node that was inserted at the head of the doubly linked list
        """
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
        """
        Insert a value at the tail of the doubly linked list

        Parameters
        ----------
        value: Any
            The value to insert

        Returns
        -------
        DoublyLinkedListNode
            The node that was inserted at the tail of the doubly linked list
        """
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
        """
        Remove a node from the doubly linked list

        Parameters
        ----------
        node: DoublyLinkedListNode
            The node to remove
        """
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

    def move_to_head(self, node: DoublyLinkedListNode) -> None:
        """
        Move a node to the head of the doubly linked list

        Parameters
        ----------
        node: DoublyLinkedListNode
            The node to move to the head of the doubly linked list
        """
        if node is self.head:
            return
        else:
            self.remove(node)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def move_to_tail(self, node: DoublyLinkedListNode) -> None:
        """
        Move a node to the tail of the doubly linked list

        Parameters
        ----------
        node: DoublyLinkedListNode
            The node to move to the tail of the doubly linked list
        """
        if node is self.tail:
            return
        else:
            self.remove(node)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def nodes(self) -> List[DoublyLinkedListNode]:
        """
        Return a list of the nodes in the doubly linked list

        Returns
        -------
        List[DoublyLinkedListNode]
            A list of the nodes in the doubly linked list
        """
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(current_node)
            current_node = current_node.next
        return nodes

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
