__version__ = "1.0.0"

class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.__repr__() 


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node_in_front_of_head(self, value):
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

    def add_node_behind_tail(self, value):
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

    def remove_node(self, node):
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


    def __iter__(self):
        self.current_iter_node = self.head
        return self

    def __next__(self):
        if self.current_iter_node is not None:
            return_node = self.current_iter_node
            self.current_iter_node = self.current_iter_node.next
            return return_node
        raise StopIteration

    def __repr__(self):
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

