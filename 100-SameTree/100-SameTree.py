# Last updated: 10/12/2026, 7:45:34 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
9        if(p == None and q == None):
10            return True
11
12        if(p == None or q == None):
13            return False
14
15        if(p.val != q.val):
16            return False
17        
18        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)