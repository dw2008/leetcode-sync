# Last updated: 10/19/2026, 7:23:19 PM
1class Solution:
2    """
3    we can initialize an array where each element represents the length of the longest valid subsequence that ends with that index. then, we can iterate through the length of the array, and at each iteration, use a second for loop to iterate through all the elements before i and check if that element is smaller than the current one; if so, set the subsequence length to the max between that element's length+1 and the current length.
4    """
5    def lengthOfLIS(self, nums: list[int]) -> int:
6        dp = [1]*len(nums)
7        for i in range(1, len(nums)):
8            for j in range(i):
9                if(nums[i] > nums[j]):
10                    dp[i] = max(dp[i], dp[j] + 1)
11        
12        return max(dp)