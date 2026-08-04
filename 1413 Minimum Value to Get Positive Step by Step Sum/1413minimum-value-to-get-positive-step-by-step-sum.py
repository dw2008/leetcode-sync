class Solution:
    """
    use prefix sum; keep track of the current prefix sum in a variable (curr). iterate through nums and 
    add each value into prefix sum one at a time. if curr is less than minVal, make curr the new 
    minVal. at the end, if minVal >= 0, just return 1. otherwise, return abs(minVal) + 1 because it's   
    the minimum value which makes prefix sum never go below 1.
    """
    def minStartValue(self, nums: List[int]) -> int:
        minVal = nums[0]
        curr = nums[0]
        
        for i in range(1, len(nums)) :
            curr += nums[i]
            if(curr < minVal) :
                minVal = curr
        
        if(minVal >= 0) :
            return 1
        
        return abs(minVal) + 1