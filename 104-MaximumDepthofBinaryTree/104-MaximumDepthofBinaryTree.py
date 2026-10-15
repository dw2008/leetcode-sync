# Last updated: 10/14/2026, 10:18:18 PM
1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def maxDepth(self, root: TreeNode | None) -> int:
10        if(root == None):
11            return 0
12        
13        curr_q = deque([root])
14        next_q = deque()
15        max_depth = 0
16
17        while(curr_q or next_q):
18            while(curr_q):
19                curr = curr_q.popleft()
20                if(curr.left):
21                    next_q.append(curr.left)
22                if(curr.right):
23                    next_q.append(curr.right)
24            max_depth += 1
25            curr_q = next_q
26            next_q = deque()
27        
28        return max_depth
29
30        