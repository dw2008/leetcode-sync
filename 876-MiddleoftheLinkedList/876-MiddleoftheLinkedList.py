# Last updated: 8/5/2026, 2:20:26 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    """
8    using slow and fast pointer; we can set the fast pointer to two times the traversal speed of the
9    slow one. if the fast pointer reaches the end, then we know that the slow pointer must be at the
10    middle since the fast is twice the speed of the slow.
11    """
12    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
13        slow = head
14        fast = head
15        
16        while fast and fast.next:
17            slow = slow.next
18            fast = fast.next.next
19        
20        return slow