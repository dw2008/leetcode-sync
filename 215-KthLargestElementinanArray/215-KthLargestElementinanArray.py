# Last updated: 9/19/2026, 6:04:56 PM
1import heapq
2
3class Solution:
4    """
5    push values onto min heap until size of heap is larger than k, then pop the
6    smallest value. keep repeating this until all numbers are pushed onto the heap,
7    then take the smallest value from there. it is impossible for the kth smallest
8    value to be popped out, so this approach works and is faster than just heapify.
9    """
10    def findKthLargest(self, nums: list[int], k: int) -> int:
11        heap = []
12        for n in nums:
13            heappush(heap, n)
14            if(len(heap) > k):
15                heappop(heap)
16        
17        return heap[0]