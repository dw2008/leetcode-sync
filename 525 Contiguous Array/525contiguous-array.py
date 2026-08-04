class Solution:
    """
    keep track of the "continuous sum" (+1 for each 1, -1 for each 0) in order to see which subarrays
    have an equal number of 0 and 1; if they do, that means their sums are the same, which we can check
    through having a hashmap of these counts and the index of their occurence. if a count is not in
    the hashmap of counts, we can create a new key/value pair of that count and its first index
    occurence. if a count is in the hashmap of counts, we can compare the current longest length of a
    subarray with the length of the subarray with the count's index in the hashmap and the current
    index. since equal counts imply an equal amount of 1s and 0s, this method works to give lengths of
    subarrays. after nums is fully examined, we can return the maximum length.
    """
    def findMaxLength(self, nums: List[int]) -> int:
        counts = dict()
        counts[0] = -1
        count = 0
        maxsum = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in counts:
                maxsum = max(maxsum, i-counts[count])
            else:
                counts[count] = i
                
        return maxsum