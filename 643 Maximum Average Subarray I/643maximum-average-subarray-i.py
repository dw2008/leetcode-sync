class Solution:
    """
    use a sliding window; first, take the sum of the window from 0 to k-1 inclusive. then, have a 
    pointer from k to len(nums) - 1 inclusive. for each loop, subtract the leftmost value from the
    current sum of the window, and add the next value on the right to the current sum of the window.
    keep track of a maximum value of the window, and then average it with k when the loops finish.
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = 0
        for i in range(k):
            current += nums[i]
            
        ans = current
        
        for i in range(k, len(nums)):
            current += nums[i] - nums[i-k]
            ans = max(ans, current)
            
        return ans / k