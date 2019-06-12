class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node):
    preorder_traversal = []
    if (node is not None):
        preorder_traversal.append(node.val)
        preorder_traversal.extend(serialize(node.left))
        preorder_traversal.extend(serialize(node.right))

    if (node is None):
        preorder_traversal.append(-1)

    return " ".join(str(x) for x in preorder_traversal)


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    print(serialize(node))


if __name__ == '__main__':
    main()