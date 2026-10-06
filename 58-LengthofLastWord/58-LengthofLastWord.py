# Last updated: 10/5/2026, 10:40:12 PM
1class Solution:
2    """
3    split string and then return length of last word
4    """
5    def lengthOfLastWord(self, s: str) -> int:
6        splitstr = s.split()
7        return len(splitstr[len(splitstr)-1])