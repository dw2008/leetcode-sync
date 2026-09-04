# Last updated: 9/4/2026, 3:22:47 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    make a dictionary with only edges that are not restricted and then just count all the traversable
6    nodes from 0 using DFS and a counter and a return etc etc whatever bro
7    """
8    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
9        neighbors = defaultdict(list)
10        restricted = set(restricted)
11        neighbors[0]
12        
13        for edge in edges:
14            if(edge[0] in restricted or edge[1] in restricted):
15                continue
16            
17            neighbors[edge[0]].append(edge[1])
18            neighbors[edge[1]].append(edge[0])
19        
20        stack = list()
21        visited = set()
22        stack.append(0)
23        count = 0
24        
25        while(stack):
26            curr = stack.pop()
27            if(curr in visited):
28                continue
29    
30            visited.add(curr)
31            
32            for neighbor in neighbors[curr]:
33                stack.append(neighbor)
34            
35            count += 1
36        
37        return count