# Last updated: 9/22/2026, 2:24:32 PM
1class Solution:
2    """
3    use a greedy approach: start from the left and flip the largest six, since only flipping a six will
4    actually increase the number. if no 6 to be flipped, return num as is. convert to str, then
5    re convert back once a number is flipped.
6    """
7    def maximum69Number (self, num: int) -> int:
8        numstr = str(num)
9        
10        for i in range(len(numstr)):
11            if(numstr[i] == '6'):
12                numstr = numstr[:i] + '9' + numstr[i+1:]
13                return int(numstr)
14        
15        return num