Problem 3
=========

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following `Node` class
```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:
```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

Asked by: Google<br>
Difficulty Level: Medium

###### Solution Steps
- [x] Use a traversal method to go through a tree and append the string to serialize it, use `-1` for leaf nodes<br>
- [x] To deserialize, split the string into list<br>
- [x] Use the same traversal order rebuild the tree<br>
- [x] Test solution
