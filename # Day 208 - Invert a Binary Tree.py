# Day 208 - Invert a Binary Tree
# DSA: Binary Tree Recursion

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


def inorder_values(root):
    if root is None:
        return []

    return (
        inorder_values(root.left)
        + [root.value]
        + inorder_values(root.right)
    )


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Before inversion:", inorder_values(root))
invert_tree(root)
print("After inversion: ", inorder_values(root))