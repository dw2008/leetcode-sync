class NumArray:
    #initialize self with a prefix sum array, so we can calculate it easier
    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums)+1)

        #avoid case where i == 0, leave a buffer so that self.sums[right + 1] doesn't go out of bounds
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)