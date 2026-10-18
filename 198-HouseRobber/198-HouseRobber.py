# Last updated: 10/18/2026, 5:56:00 PM
1from functools import cache
2
3class Solution:
4    """
5    using DP: for each house, we can decide what to rob based on the values of the previous houses if we do rob them. we can memorize the past values for houses and use recursion to calculate any cases that are not memorized. for base cases, we can have i = 0 (return 1st element), i = 1 (max of 1st and 2nd elements) and take the max of the i-1 and i-2 recursions otherwise. the time complexity for this is O(n) where n is the length of nums because we only visit each state once and then memorie it after, where access is O(1).
6    """
7    def rob(self, nums: list[int]) -> int:
8        @cache
9        def dp(i):
10            if(i == 0):
11                return nums[0]
12            if(i == 1):
13                return max(nums[0], nums[1])
14
15            return max(dp(i-1), dp(i-2) + nums[i]) #dp(i-1) will make nums[i] invalid to add
16        
17        return dp(len(nums)-1)