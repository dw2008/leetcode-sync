class Solution:
    """
    just use a prefix sum and keep an array that is the sum of every value up to that index
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [nums[0]]
        
        for i in range(1, len(nums)):
            sums.append(sums[i-1] + nums[i])
        
        return sums
    