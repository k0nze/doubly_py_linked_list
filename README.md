# Doubly (Py) Linked List 1️⃣ ↔️ 2️⃣ ↔️ 3️⃣

[![CI](https://github.com/k0nze/mesi_cachesim/actions/workflows/ci.yml/badge.svg)](https://github.com/k0nze/doubly_py_linked_list/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

A module that implements doubly linked lists in python

## Example

```
python -m pip install doubly-py-linked-list
```

```python
>>> from doubly_py_linked_list import DoublyLinkedList as dll
>>> d = dll([1, 2, 3, 4])
>>> d
1 <-> 2 <-> 3 <-> 4
>>> node_0 = d.insert_head(0)
>>> node_5 = d.insert_tail(5)
>>> for v in d:
...     print(v)
...
0
1
2
3
4
5
>>> d.move_to_head(node_5)
>>> d.move_to_tail(node_0)
>>> list(d)
[5, 1, 2, 3, 4, 0]
>>> d.pop_head()
5
>>> list(d)
[1, 2, 3, 4, 5, 0]
>>> d.pop_tail()
0
>>> list(d)
[1, 2, 3, 4]
>>> d.nodes(d)
[ddl_node(1), ddl_node(2), ddl_node(3), ddl_node(4)]
```
