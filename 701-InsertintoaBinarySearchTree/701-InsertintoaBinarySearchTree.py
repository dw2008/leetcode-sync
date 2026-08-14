# Last updated: 8/14/2026, 1:06:21 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    """
9    keep traversing through the BST until the next node to go to is null. then, set the next node as
10    the node to insert and return the resulting tree.
11    """
12    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
13        if not root:
14            return TreeNode(val, None, None)
15        
16        def helper(node):
17            if val > node.val:
18                if not node.right:
19                    node.right = TreeNode(val, None, None)
20                    return
21                return helper(node.right)
22            else:
23                if not node.left:
24                    node.left = TreeNode(val, None, None)
25                    return
26                return helper(node.left)
27        
28        helper(root)
29        return root