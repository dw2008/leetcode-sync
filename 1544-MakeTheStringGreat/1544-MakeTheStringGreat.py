# Last updated: 8/7/2026, 10:58:26 AM
1class Solution:
2    """
3    using stack, push each character one at a time into the stack. when pushing in, check the previous
4    character and see if it's "bad", if it is, dont add it and pop the other character. at the end,
5    concatenate and return string.
6    """
7    def makeGood(self, s: str) -> str:
8        splitstr = list(s)
9        stack = []
10        
11        for c in splitstr:
12            if len(stack) == 0:
13                stack.append(c)
14                continue
15                
16            top = stack[-1]
17            if top != c and top.upper() == c.upper():
18                stack.pop()
19            else:
20                stack.append(c)
21        
22        return ''.join(stack)