# Last updated: 8/28/2026, 8:25:18 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    first, iterate through all the edges and put all bidirectional connections in a hashmap of
6    neighbors. then, starting from source, add all neighbors into a stack and check traversed nodes
7    with a set; if destination is found return true, otherwise return false if stack is empty.
8    """
9    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
10        if(source == destination):
11            return True
12
13        neighbors = defaultdict(list)
14        
15        for edge in edges:
16            neighbors[edge[0]].append(edge[1])
17            neighbors[edge[1]].append(edge[0])
18            
19        stack = list()
20        stack.append(source)
21        traversed = set()
22        
23        while(len(stack) > 0):
24            current = stack.pop()
25            if(current in traversed):
26                continue
27            
28            for neighbor in neighbors[current]:
29                if(neighbor == destination):
30                    return True
31                stack.append(neighbor)
32            traversed.add(current)
33            
34        return False