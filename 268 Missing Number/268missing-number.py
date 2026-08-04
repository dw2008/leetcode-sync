class Solution:
    """
    using hashmap; create a set from nums and iterate through the range (which would be 0 to len(nums)
    inclusive because you need [0,n]) and see which number is not there.
    """
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = set(nums)
        
        for i in range(len(nums)+1):
            if i not in hashmap:
                return i