# Last updated: 9/2/2026, 4:07:50 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    since each 1 on the map basically has up to 4 neighbors we can make a dictionary of each node and
6    its neighbors, then go through each of the nodes and DFS through them and find the max length
7    and don't consider a node thats already been visited through dfs; then return the max length
8    of an island
9    """
10    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
11        neighbors = defaultdict(list)
12        
13        for i in range(len(grid)):
14            for j in range(len(grid[i])):
15                if(grid[i][j] == 0):
16                    continue
17                    
18                neighbors[(i, j)]
19                
20                if(i > 0 and grid[i-1][j] == 1):
21                    neighbors[(i,j)].append((i-1, j))
22                
23                if(i < len(grid) - 1 and grid[i+1][j] == 1):
24                    neighbors[(i, j)].append((i+1, j))
25                
26                if(j > 0 and grid[i][j-1] == 1):
27                    neighbors[(i, j)].append((i, j-1))
28                
29                if(j < len(grid[i]) - 1 and grid[i][j+1] == 1):
30                    neighbors[(i, j)].append((i, j+1))
31        
32        if(len(neighbors) == 0):
33            return 0
34        
35        result = 0
36        visited = set()
37        
38        for location in neighbors:
39            if(location in visited):
40                continue
41                
42            stack = list()
43            stack.append(location)
44            count = 0
45            
46            while(len(stack) > 0):
47                curr = stack.pop()
48                if(curr in visited):
49                    continue
50                    
51                visited.add(curr)
52                for neighbor in neighbors[curr]:
53                    stack.append(neighbor)
54                    
55                count += 1
56                
57            result = max(result, count)
58        
59        return result