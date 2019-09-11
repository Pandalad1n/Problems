# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def tree_pass(node):
            if node:
                vals.append(node.val)
                tree_pass(node.left)
                tree_pass(node.right)

        tree_pass(root)
        return len(set(vals)) == 1


r = TreeNode(1)
r.left = TreeNode(1)
r.right = TreeNode(1)
print(Solution().isUnivalTree(r))