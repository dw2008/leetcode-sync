class Solution:
    #input: list of ints with definite length
    #output: leftmost pivot index (all numbers strictly left sum up to sum of all numbers strictly right of pivot), return -1 if no pivot exists
    #strategy: since we return the leftmost pivot, we can just use two sliding windows. the left one will be from 0 to i - 1, and the right one will be from i + 1 to len(nums). for the left, we can set sum as 0, but for right, we want the sum to be the sum of the array excluding the first element. we can expand the left by 1 and contract the right by 1 every incrementation and return i if pivot found. if not found, return -1.
    #edge cases: if not found, return -1 at the end.
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = 0

        for i in range(1, len(nums)):
            rightSum += nums[i]

        for i in range(len(nums)):
            if rightSum == leftSum:
                return i
            
            leftSum += nums[i]
            if i < len(nums)-1:
                rightSum -= nums[i+1]

        return -1