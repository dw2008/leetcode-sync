# Last updated: 10/1/2026, 2:36:41 PM
1class Solution:
2    """
3    using binary search: first guess a maximum subarray sum in between the smallest possible sum
4    and the largest possible sum. then go iterate through the array and try to create subarrays that
5    are less than or equal to the guessed sum. if we reach the end of the array and the amount of
6    subarrays is less than or equal to k, then we know that we have a feasible answer and we can keep
7    track of that and try smaller minimums. if the amount of subarrays is greater than k, our min is
8    too small and we have to try larger minimums. we can return the smallest valid minimum that we
9    can find.
10    """
11    def splitArray(self, nums: list[int], k: int) -> int:
12        left = max(nums)
13        right = sum(nums)
14        result = sum(nums)
15        
16        while left <= right:
17            mid = (left + right) // 2
18            current_sum = 0
19            subarrays_created = 1
20            
21            for n in nums:
22                if current_sum + n > mid:
23                    subarrays_created += 1
24                    current_sum = 0
25                current_sum += n
26            
27            if subarrays_created <= k:
28                result = mid
29                right = mid - 1
30            
31            else:
32                left = mid + 1
33        
34        return result