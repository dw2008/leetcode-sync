# Last updated: 10/8/2026, 8:28:06 PM
1class Solution:
2    """
3    using backtracking: for each position, see if the digit is valid given the previous digit (always
4    valid for the first digit). then, add that digit to the path -> move to next position. when
5    backtracking, pop the digit out and try the next digit. for a digit to be valid, it has to have
6    either a possible digit that is smaller or a possible digit that is larger.
7    """
8    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
9        result = []
10        
11        def backtrack(prev, path):
12            if(len(path) == n):
13                result.append(int(path[:]))
14                return
15            
16            for i in range(10):
17                if abs(prev - i) == k:
18                    path += str(i)
19                    backtrack(i, path)
20                    path = path[:-1]
21            
22        for i in range(1,10):
23            if(i-k >= 0 or i+k<10):
24                backtrack(i, str(i))
25        
26        return result