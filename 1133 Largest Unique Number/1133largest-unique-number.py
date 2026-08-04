class Solution:
    """
    using hashmap; get the count of how many time each element appears in num. then, go through the 
    hashmap and get the largest value that has one occurence.
    """
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        
        res = -1
        for key, value in hashmap.items():
            if value == 1 and key > res:
                res = key
        
        return res