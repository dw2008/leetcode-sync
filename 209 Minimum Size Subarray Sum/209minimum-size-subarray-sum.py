class Solution:
    #input: minimum int length of a subarray target, and an array nums
    #output: minimal length of subarray with sum >= target
    #strategy: use sliding window approach to comb through the array. adjust right index until sum >= target (if length of subarray less than minimum, make new minimum), then adjust left index array until sum <= target and repeat until right index hits len(nums). then return minimum
    #edge cases: if there is no such subarray that greater than or equal to target
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = len(nums)
        left = 0
        subsum = 0
        
        test = 0
        for i in range(len(nums)):
            test += nums[i]
        if test < target:
            return 0

        for right in range(0, len(nums)):
            subsum += nums[right]
            while subsum >= target:
                minlen = min(minlen, right-left+1)
                subsum -= nums[left]
                left += 1
        
        return minlen