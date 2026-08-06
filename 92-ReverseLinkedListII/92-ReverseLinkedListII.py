# Last updated: 8/6/2026, 1:19:08 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    """
8    use two pointers () to point to the start . then, iterate through the
9    section to reverse the pointers for each node. return the head (or the new head, keep it updated through
10    iterations). also edge case where empty list ujst return None. anchor is there to point to before 
11    the reversed portion so it can update the connection at the end. tail is there to point to the node at the
12    end of the reversed portion so it can then set the end's next to current, since current would go past tail.
13    """
14    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
15        if not head:
16            return None
17        
18        current = head
19        prev = None
20        for i in range(left-1):
21            prev = current
22            current = current.next
23        
24        tail = current
25        anchor = prev
26        for i in range(right-left+1):
27            temp = current.next
28            current.next = prev
29            prev = current
30            current = temp
31        
32        if anchor:
33            anchor.next = prev
34        else:
35            head = prev
36        tail.next = current
37        return head