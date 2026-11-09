# Last updated: 11/8/2026, 9:40:54 PM
1class Solution:
2    def hammingDistance(self, x: int, y: int) -> int:
3        return bin(x^y).count('1')