# Last updated: 8/11/2026, 5:45:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    """
9    search through the tree and for each node, find the lengths of the left and right branches. keep
10    a global variable that tracks the maximum diameter, and update the diameter (left + right + 1) for
11    each node. after going through a node, return the maximum depth between the left and right branches
12    and then repeat until every node has been compared.
13    """
14    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
15        if not root:
16            return 0
17        maxdiam = 0
18        
19        def helper(node) -> int:
20            if not node:
21                return 0
22            nonlocal maxdiam
23            print(node.val)
24            left = helper(node.left)
25            right = helper(node.right)
26            maxdiam = max(maxdiam, left + right)
27            
28            return max(left, right) + 1
29        
30        helper(root)
31        return maxdiam
32            