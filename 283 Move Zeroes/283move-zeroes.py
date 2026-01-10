class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        #input: list of nums; output: no output, must modify array in place
        #strategy: TWO POINTERS; use a pointer (i) to iterate through the input array. while doing so, have another pointer (zero) represent the position of the frontmost zero, then swap nums[zero] with nums[i] if nums[i] is nonzero. this will bring the non-zeroes to the front, and we can increment j when we do so. we can keep doing this for the whole array
        #test case: 0, 1, 0, 3, 12
        #currently no exceptions visible, since nums has a definite length and each value of nums is an integer
        for i in range(len(nums)) :
            if nums[i] != 0:
                #can use tuple unpacking here#
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        
        return nums