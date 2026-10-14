# Last updated: 10/13/2026, 10:09:10 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        q = deque([root, root])
10        
11        while q:
12            t1 = q.popleft()
13            t2 = q.popleft()
14            if(t1 is None and t2 is None):
15                continue
16            if(t1 is None or t2 is None):
17                return False
18            if(t1.val != t2.val):
19                return False
20            q.append(t1.left)
21            q.append(t2.right)
22            q.append(t1.right)
23            q.append(t2.left)
24
25        return True