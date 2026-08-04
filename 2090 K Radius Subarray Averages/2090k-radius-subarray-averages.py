class Solution:
    """
    using prefix sum; keep track of all k-radius averages in an array. first by default put -1 in each
    index. then, if k*2 is out of bounds, return the entire array with -1 by default. otherwise,
    compute the first average that is not -1 and put it in the averages array. then, iterate through
    the array until pointer = len(nums)-k (reached the end), keeping track of the prefix sum. for each
    index, first update the prefix sum by adding the current value while subtracting the leftmost value
    and add the average to the average array. then return the average array.
    """
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = []
        
        for i in range(0, len(nums)):
            averages.append(-1)
        
        sums = 0
        for i in range(0, 2*k+1):
            if(i >= len(nums)):
                return averages
            sums += nums[i]
        averages[k] = sums//(k*2+1)
        
        for i in range(k+1, len(nums)-k):
            sums += nums[i+k] - nums[i-k-1]
            averages[i] = sums//(k*2+1)
        
        return averages