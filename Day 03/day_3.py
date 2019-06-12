class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Answer was
# root l e f t   l   e   f   t   .   l   e   f   t       -       1       -       1   -   1 r i g h t   -   1   -   1
# Because the return is a string
# def serialize(node: Node):
#     preorder_traversal = []
#     if (node is not None):
#         preorder_traversal.append(node.val)
#         preorder_traversal.extend(serialize(node.left))
#         preorder_traversal.extend(serialize(node.right))

#     if (node is None):
#         preorder_traversal.append(-1)

#     return " ".join(str(x) for x in preorder_traversal)


def preorder_traverse(node: Node):
    preorder_traversal = []
    if (node is not None):
        preorder_traversal.append(node.val)
        preorder_traversal.extend(preorder_traverse(node.left))
        preorder_traversal.extend(preorder_traverse(node.right))

    if (node is None):
        preorder_traversal.append(-1)

    return preorder_traversal


def build_tree(tree_list: list):
    if len(tree_list) is not 0:
        val = tree_list.pop(0)
        if val is not -1:
            return Node(val, build_tree(tree_list), build_tree(tree_list))
    else:
        return Node(None)


def serialize(node: Node):
    preorder_traversal = preorder_traverse(node)
    return " ".join(str(x) for x in preorder_traversal)


def deserialize(tree_str: str):
    tree_list = tree_str.split(" ")
    node = build_tree(tree_list)
    return node


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    print(deserialize(serialize(node)).left.left.val)


if __name__ == '__main__':
    main()