# Last updated: 10/2/2026, 12:20:20 PM
1class Solution:
2    """
3    use recursion + backtracking. first, select one number of the array. then,
4    select the next number of the array, and so on. once the end is reached (like
5    traversing a tree), we can backtrack and check the other possibilities. after
6    done, return the resulting array from appending copies of the results.
7    """
8    def permute(self, nums: list[int]) -> list[list[int]]:
9        def backtrack(curr):
10            if(len(nums) == len(curr)): #if all numbers have been added
11                result.append(curr[:]) #construct a separate arr
12                return
13            for n in nums:
14                if n not in curr: #if the current number has not been added
15                    curr.append(n)
16                    backtrack(curr)
17                    curr.pop() #backtracking so we can look at the next #
18        
19        result = []
20        backtrack([])
21        return result