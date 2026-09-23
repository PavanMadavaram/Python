# Day 207 - Kth Smallest Element in a BST
# DSA: Binary Search Tree + Inorder Traversal

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def kth_smallest(root, k):
    stack = []
    current = root

    while True:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.value

        current = current.right


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

print("3rd smallest value:", kth_smallest(root, 3))