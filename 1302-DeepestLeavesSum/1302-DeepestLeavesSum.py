# Last updated: 8/13/2026, 2:27:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9class Solution:
10    """
11    using BFS, traverse through the tree. we can check if a level is the last level by keeping track of two 
12    queues: current and next level. if nextis empty, we can sum all values in current.
13    """
14    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
15        nextlevel = deque([root]) 
16
17        while nextlevel:
18            curr = nextlevel
19            nextlevel = deque()
20            for node in curr:
21                if node.left:
22                    nextlevel.append(node.left)
23                if node.right:
24                    nextlevel.append(node.right)
25        
26        return sum([node.val for node in curr])