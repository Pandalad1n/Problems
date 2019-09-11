class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k):
    prev = None
    for iter in walk_tree(root_node):
        if iter >= k:
            return prev, iter
        prev = iter


def walk_tree(node):
    if node.left:
        yield from walk_tree(node.left)

    yield node.value

    if node.right:
        yield from walk_tree(node.right)


root = Node(8)
# root.left = Node(4)
# root.right = Node(12)
#
# root.left.left = Node(2)
# root.left.right = Node(6)
#
# root.right.left = Node(10)
# root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
