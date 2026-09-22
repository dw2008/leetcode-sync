# Last updated: 9/21/2026, 9:02:43 PM
1import heapq
2
3"""
4since stack + heap approach gives tle, need to make a better solution. first set up nums as a min heap,
5by calling the add function for each element of nums.
6when adding, if the size of the heap is less than k or if the value is greater than the kth greatest,
7we can add the new value to the heap and remove the smallest value if the heap size is now greater than
8k. this will always ensure that the smallest value will be the kth largest value overall, as everything 
9smaller than the kth largest value will not affect the kth largest value's position, so we can just
10ignore that and not add it to the heap.
11"""
12class KthLargest:
13
14    def __init__(self, k: int, nums: list[int]):
15        self.nums = list()
16        self.k = k
17        
18        for num in nums:
19            self.add(num)
20        
21    def add(self, val: int) -> int:
22        if(len(self.nums) < self.k or val > self.nums[0]):
23            heappush(self.nums, val)
24            if(len(self.nums) > self.k):
25                heappop(self.nums)
26        
27        return self.nums[0]
28
29
30# Your KthLargest object will be instantiated and called as such:
31# obj = KthLargest(k, nums)
32# param_1 = obj.add(val)