# Last updated: 10/17/2026, 7:43:10 PM
1class Solution:
2    """
3    going backwards just add 1 and increment following digits if needed
4    """
5    def plusOne(self, digits: list[int]) -> list[int]:
6        i = len(digits)-1
7        digits[i] += 1
8        while(digits[i] == 10 and i > 0):
9            digits[i] = 0
10            digits[i-1] += 1
11            i -= 1
12        if(digits[0] == 10):
13            digits[0] = 0
14            digits.insert(0, 1)
15        return digits