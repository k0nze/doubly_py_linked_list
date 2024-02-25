# Doubly (Py) Linked List 1️⃣ ↔️ 2️⃣ ↔️ 3️⃣

A module that implements doubly linked lists in python

## Example

```
python -m pip install doubly_py_linked_list
```

```python
from doubly_py_linked_list import doubly_py_linked_list as dll

d = dll()

node_1 = d.insert_tail(1)
node_2 = d.insert_head(2)
node_3 = d.insert_tail(3)
node_4 = d.insert_tail(3)

for v in dll:
    print(v)

d.move_to_head(node_3)
d.move_to_tail(node_1)

l = list(d)

d.remove(node_1)
d.remove(node_2)
d.remove(node_3)
d.remove(node_4)
```
