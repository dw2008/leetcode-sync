# Last updated: 9/29/2026, 7:10:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9        res = []
10        self.helper(root, res)
11        return res
12
13    def helper(self, root, res):
14        if root is not None:
15            self.helper(root.left, res)
16            res.append(root.val)
17            self.helper(root.right, res)
18