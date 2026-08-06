# Last updated: 8/6/2026, 11:37:46 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    """
8    iterating through the linked list, make each node point to the previous node by keeping track of the 
9    previous and next nodes and then return the new head.
10    """
11    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
12        previous = None
13        current = head
14
15        while current:
16            nextnode = current.next
17            current.next = previous
18            previous = current
19            current = nextnode
20        
21        return previous