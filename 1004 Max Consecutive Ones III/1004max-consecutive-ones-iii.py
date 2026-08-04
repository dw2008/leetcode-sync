class Solution:
    """
    use a sliding window; have a left pointer and a right pointer corresponding to that window. for
    each window snapshot, keep track of the number of zeroes. if after expanding the window the number 
    of zeroes is greater than k, shrink the window until the number of zeroes is equal to k. keep track
    of and return the largest window size (which is the largest number of ones in a row).
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        zeroes = 0
        
        for right in range(len(nums)):
            if(nums[right] == 0):
                zeroes += 1
            
            while zeroes > k:
                if(nums[left] == 0):
                    zeroes -= 1
                left += 1
            
            ans = max(right - left + 1, ans)
        
        return ans