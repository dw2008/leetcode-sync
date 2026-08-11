# Last updated: 8/10/2026, 6:06:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    """
9    for every node, first check if the root is None. if so, return 0. then, if the
10    left of the current node is None, return the result from the right node + 1. do
11    the same but the other way. otherwise, if neither child is none, choose the min
12    between them and return that value + 1.
13    """
14    def minDepth(self, root: Optional[TreeNode]) -> int:
15        def minDepthHelper(curr: Optional[TreeNode]) -> int:
16            if curr is None:
17                return 0
18        
19            if curr.left is None:
20                return minDepthHelper(curr.right) + 1
21            elif curr.right is None:
22                return minDepthHelper(curr.left) + 1
23            
24            return min(minDepthHelper(curr.left), minDepthHelper(curr.right)) + 1
25        return minDepthHelper(root)