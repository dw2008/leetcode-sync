# Last updated: 8/31/2026, 10:20:39 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    first make a hashmap of each node and its neighbors. then make a hashmap of each node and whether
6    or not its visited or not yet (default start at 0). then start at any node and then do dfs and
7    put stack yada yada and then if the stack has run out but not all nodes are visited then go to the
8    nodes that havent been visited and keep doing dfs until every node is visited. then count the
9    amount of times u had to start dfs and then return.
10    """
11    def countComponents(self, n: int, edges: List[List[int]]) -> int:
12        neighbors = defaultdict(list)
13        visited = set()
14        count = 0
15        
16        for edge in edges:
17            neighbors[edge[0]].append(edge[1])
18            neighbors[edge[1]].append(edge[0])
19        
20        for node in range(n):
21            if(node in visited):
22                continue
23                
24            stack = list()
25            stack.append(node)
26            visited.add(node)
27            
28            while len(stack) > 0:
29                curr = stack.pop()
30                visited.add(curr)
31                
32                for neighbor in neighbors[curr]:
33                    if(neighbor not in visited):
34                        stack.append(neighbor)
35                    
36            count += 1
37        
38        return count