# Last updated: 8/13/2026, 2:56:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8
9class Solution:
10    """
11    just use bfs but reverse the queue every other iteration when adding to the result list
12    """
13    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
14        if not root:
15            return []
16        res = list()
17        queue = deque([root])
18        reverse = False
19        
20        while queue:
21            n = len(queue)
22            
23            if not reverse:
24                res.append([node.val for node in queue])
25            else:
26                res.append([node.val for node in reversed(queue)])
27                
28            for i in range(n):
29                node = queue.popleft()
30                if node.left:
31                    queue.append(node.left)
32                if node.right:
33                    queue.append(node.right)
34            reverse = not reverse
35        
36        return res