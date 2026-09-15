# Last updated: 9/15/2026, 2:56:31 PM
1import math
2from collections import defaultdict
3
4class Solution:
5    """
6    first make a hashmap of each bomb and its neighbors (only connect if radius of one bomb is greater 
7    than or equal to the distance betwen two bombs, then perform dfs
8    on each bomb and see how many bombs it will detonate
9    """
10    def maximumDetonation(self, bombs: List[List[int]]) -> int:
11        neighbors = defaultdict(list)
12        no_bombs = defaultdict(int)
13        
14        for i in range(0, len(bombs)):
15            b1 = (bombs[i][0], bombs[i][1], bombs[i][2])
16            no_bombs[b1] += 1
17            for j in range(i + 1, len(bombs)):
18                b2 = (bombs[j][0], bombs[j][1], bombs[j][2])
19                neighbors[b1]
20                neighbors[b2]
21                distance = math.sqrt((b1[0]-b2[0])**2 + (b1[1]-b2[1])**2)
22                
23                if(b1[2] >= distance):
24                    neighbors[b1].append(b2)
25                
26                if(b2[2] >= distance):
27                    neighbors[b2].append(b1)
28        
29        result = 0
30        if(not neighbors):
31            return 1
32        
33        for bomb in neighbors:
34            visited = set()
35            stack = list()
36            stack.append(bomb)
37            temp = 0
38            
39            while(stack):
40                curr = stack.pop()
41                if(curr in visited):
42                    continue
43                visited.add(curr)
44                temp += no_bombs[curr]
45                
46                for neighbor in neighbors[curr]:
47                    if(neighbor not in visited):
48                        stack.append(neighbor)
49            
50            if(temp > result):
51                result = temp
52        
53        return result