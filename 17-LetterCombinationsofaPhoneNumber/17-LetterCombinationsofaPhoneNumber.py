# Last updated: 10/6/2026, 3:53:33 PM
1class Solution:
2    """
3    backtracking: for each digit, add on a letter to a "path" string (depending on the digit) and go
4    to the next digit; keep going until all possible paths are reached. when reaching the end of
5    digits, then we can start backtracking.
6    """
7    def letterCombinations(self, digits: str) -> list[str]:
8        result = []
9        letters = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],
10                   ["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
11        
12        def backtrack(index: int, path: str):
13            if(index == len(digits)):
14                result.append(path)
15                return
16            
17            for l in letters[int(digits[index])]:
18                path += l
19                backtrack(index + 1, path)
20                path = path[:-1]
21        
22        backtrack(0, "")
23            
24        return result