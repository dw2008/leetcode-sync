# Last updated: 10/10/2026, 4:24:16 PM
1class Solution:
2    """
3    using backtracking: loop through all numbers 1-9 and add numbers to a list, keeping track of the
4    sum of the list. if the sum goes over n or there are k numbers in the list with the sum less than
5    n, the combination is invalid and we can skip. if there are k numbers in the list which sum to n,
6    then we can append that list to the result.
7    """
8    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
9        result = []
10        
11        def backtrack(total: int, curr, start: int):
12            if(len(curr) > k or total > n):
13                return
14            
15            if(len(curr) == k and total == n):
16                curr.sort()
17                if(curr not in result):
18                    result.append(curr[:])
19            
20            for i in range(start + 1, 10):
21                if(total + i <= n):
22                    curr.append(i)
23                    backtrack(total+i, curr, i)
24                    curr.pop()
25                    
26        backtrack(0, [], 0)
27        return result;