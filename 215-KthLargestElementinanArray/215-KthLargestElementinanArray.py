# Last updated: 9/19/2026, 5:58:48 PM
1import heapq
2
3class Solution:
4    """
5    use a reversed min heap? i dont know if that considered sorting lol just pop k times? idk man
6    """
7    def findKthLargest(self, nums: list[int], k: int) -> int:
8        for i in range(len(nums)):
9            nums[i] = nums[i] * -1
10            
11        heapify(nums)
12        curr = 0
13        
14        for i in range(k):
15            curr = heappop(nums)
16        
17        return curr * -1