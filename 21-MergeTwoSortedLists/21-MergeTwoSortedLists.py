# Last updated: 8/30/2026, 11:07:59 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    """
8    use two pointers to traverse list1 and list2 simultaneously and then just make
9    smaller one point to the larger one after setting a temp pointer to the next
10    value so it isnt lost and then return the original head pointer
11    """
12    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
13        dummy = ListNode()
14        tail = dummy
15
16        while list1 and list2:
17            if list1.val <= list2.val:
18                tail.next = list1
19                list1 = list1.next
20            else:
21                tail.next = list2
22                list2 = list2.next
23            tail = tail.next
24
25        tail.next = list1 or list2
26        return dummy.next