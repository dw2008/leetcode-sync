# Last updated: 8/6/2026, 1:16:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    """
8    use two pointers () to point to the start . then, iterate through the
9    section to reverse the pointers for each node. return the head (or the new head, keep it updated through
10    iterations). also edge case where empty list ujst return None
11    """
12    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
13        if not head:
14            return None
15        
16        current = head
17        prev = None
18        for i in range(left-1):
19            prev = current
20            current = current.next
21        
22        tail = current
23        anchor = prev
24        for i in range(right-left+1):
25            temp = current.next
26            current.next = prev
27            prev = current
28            current = temp
29        
30        if anchor:
31            anchor.next = prev
32        else:
33            head = prev
34        tail.next = current
35        return head