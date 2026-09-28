# Last updated: 9/28/2026, 6:18:32 PM
1class Solution:
2    """
3    we can optimize this solution by performing binary search starting from 1 to the maximum element
4    in nums. the reason why we do this is because instead of dividing starting from 1 and incrementing
5    by 1, if we divide and sum and exceeds the threshold, then we know that the divisor and everything
6    below it is too small. if the sum is less than/equal to the threshold, we know that the divisor
7    is valid, but there may be a smaller value that is also valid; we can keep track of the current
8    smallest valid divisor and return that at the end.
9    """
10    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
11        left = 1
12        right = max(nums)
13        result = -1
14        
15        while(left <= right):
16            mid = (left + right) // 2
17            total = 0
18            for num in nums:
19                total += math.ceil(num/mid)
20            
21            if(total <= threshold):
22                result = mid
23                right = mid - 1
24            
25            if(total > threshold):
26                left = mid + 1
27        
28        return result