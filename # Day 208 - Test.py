# Day 208 - Test

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def preorder_values(root):
    if root is None:
        return []

    return (
        [root.value]
        + preorder_values(root.left)
        + preorder_values(root.right)
    )


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

assert preorder_values(root) == [4, 2, 1, 3, 7, 6, 9]

invert_tree(root)

assert preorder_values(root) == [4, 7, 9, 6, 2, 3, 1]
assert invert_tree(None) is None

print("Day 208 test ok")