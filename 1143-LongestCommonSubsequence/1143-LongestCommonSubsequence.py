# Last updated: 10/24/2026, 4:55:47 PM
1from functools import cache
2class Solution:
3    """
4    using dp, we can treat this as a combination of two pointers and dp. for each matching character, we can increment a counter. we can then choose to either move forward in str1 or str2 if the character doesnt match, and we can do both while keeping track of which path leads to the best outcome overall.
5    """
6    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
7        @cache
8        def dp(i: int, j: int):
9            if i == len(text1) or j == len(text2):
10                return 0
11            if text1[i] == text2[j]:
12                return dp(i+1, j+1) + 1
13            else:
14                return max(dp(i+1, j), dp(i, j+1))
15        
16        return dp(0, 0)