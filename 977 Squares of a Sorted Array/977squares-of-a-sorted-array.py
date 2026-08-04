class Solution:
    """
    use two pointers; left points to the most negative element and right points to the most positive 
    initially. until each element in nums is processed, compare nums[left] and nums[right]. square the
    max value between abs(nums[left]) and abs(nums[right]) and put it to the rightmost not occupied 
    element of a new array, increment/decrement left/right respectively.
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        res = [None]*len(nums)
        
        for i in range(len(nums)):
            print(i)
            if(abs(nums[left]) > abs(nums[right])):
               res[len(nums)-1-i] = nums[left]**2
               left += 1
            else:
               res[len(nums)-1-i] = nums[right]**2
               right -= 1
        
        return res