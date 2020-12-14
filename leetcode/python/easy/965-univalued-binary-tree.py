# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverseAndAdd(node, s):
    s.add(node.val)
    if node.left is not None:
        traverseAndAdd(node.left, s)
    if node.right is not None:
        traverseAndAdd(node.right, s)
    return

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        s = set()
        traverseAndAdd(root, s)
        return len(s) == 1
