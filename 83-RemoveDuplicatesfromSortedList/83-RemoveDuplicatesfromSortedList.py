# Last updated: 8/5/2026, 2:27:38 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    """
8    possible hashmap solution, but will just use while loop; for each node, while the next node is
9    the same value, delete it and then when not same traverse to next node. this wont use as much
10    memory as the hashmap solution
11    """
12    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
13        pointer = head
14        
15        while pointer:
16            while pointer.next and pointer.next.val == pointer.val:
17                pointer.next = pointer.next.next
18            pointer = pointer.next
19        
20        return head