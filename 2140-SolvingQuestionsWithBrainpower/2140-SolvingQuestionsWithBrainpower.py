# Last updated: 10/20/2026, 2:20:59 PM
1from functools import cache
2
3class Solution:
4    """
5    for each question solved, we can earn points but cannot earn the points for the next brainpower questions, which means that the points we can earn for a question is the points at the current locaiton + the possible points earned at or after the next available questions. therefore, we can recurse and take the maximum between taking the question and not taking the question for every index.
6    """
7    def mostPoints(self, questions: list[list[int]]) -> int:
8        @cache
9        def dp(i):
10            if(i >= len(questions)):
11                return 0
12            return max(questions[i][0] + dp(i+questions[i][1]+1), dp(i+1))
13        return dp(0)