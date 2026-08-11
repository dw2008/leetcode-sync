# Last updated: 8/11/2026, 4:43:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    """
9    for each ancestor and node, we know they have the correct ancestor-node relation.
10    therefore, we can just return the minimum and maximum differences between left
11    and right subtrees and store the current min/max as a variable in the recursive
12    function. we can acheive this with a helper function with parameters of the
13    current node, current min, and current max.
14    """
15    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
16        if not root:
17            return 0
18        
19        def maxAncestorDiffHelper(node: Optional[TreeNode], maxval: int, minval: int) -> int:
20            if not node:
21                return maxval-minval
22            
23            maxval = max(maxval, node.val)
24            minval = min(minval, node.val)
25            left = maxAncestorDiffHelper(node.left, maxval, minval)
26            right = maxAncestorDiffHelper(node.right, maxval, minval)
27            return max(left,right)
28        
29        return maxAncestorDiffHelper(root, root.val, root.val)