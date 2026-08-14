# Last updated: 8/14/2026, 1:17:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    """
9    traverse bst (try to find the target value) and put the traversal order in an array. afterwards,
10    traverse the array and find the smallest closest value to return.
11    """
12    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
13        options = list()
14        found = False
15        
16        def search(node):
17            options.append(node.val)
18            
19            if target == node.val:
20                found = True
21                return
22            
23            if target > node.val:
24                if not node.right:
25                    return
26                return search(node.right)
27            else:
28                if not node.left:
29                    return
30                return search(node.left)
31        
32        search(root)
33        closest = options[0]
34        
35        for val in options:
36            if abs(target - val) == abs(target - closest):
37                closest = min(closest, val)
38            elif abs(target-val) < abs(target - closest):
39                closest = val
40        
41        return closest