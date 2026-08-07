# Last updated: 8/7/2026, 10:45:51 AM
1class Solution:
2    """
3    first, separate the path by '/'. then, check each directory/file name and push into a stack if not
4    empty, '.', or '..'. if the name is '.', do nothing. if the name is '..', pop item out of stack.
5    convert stack into a string and then return the result.
6    """
7    def simplifyPath(self, path: str) -> str:
8        stack = []
9        splitpath = path.split('/')
10        
11        for item in splitpath:
12            if item == '' or item == '.':
13                continue
14            elif item == '..':
15                if len(stack) > 0:
16                    stack.pop()
17            else:
18                stack.append(item)
19            
20        return '/'+ '/'.join(stack)