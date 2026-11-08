# Last updated: 11/7/2026, 6:48:34 PM
1class Solution:
2    """
3    something that we can do because of XOR's property is that since x XOR x = 0, we can create a mask and keep XORing every value in the list. that means every single duplicate value will cancel each other out, leaving only the single value within the mask. this is the same big O as checking every number and putting it in a hashmap, but its O(1) space instead of O(n).
4    """
5    def singleNumber(self, nums: list[int]) -> int:
6        mask = 0
7        for num in nums:
8            mask ^= num
9        return mask