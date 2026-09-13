# Last updated: 9/13/2026, 5:41:31 PM
1from collections import deque
2
3class Solution:
4    """
5    starting at the origin, each point's neighbors are the positions reachable by dice rolls, in the
6    form n corresponding to square #. before doing search convert board into a flat array in order to
7    not have to deal with the index math. then just do regular BFS where each neighbor of a node is
8    the 6 possible other nodes to reach with a dice roll. when final area is reached, return count + 1.
9    """
10    def snakesAndLadders(self, board: List[List[int]]) -> int:
11        flat = list()
12        
13        for i, row in enumerate(reversed(board)):
14            if(i%2 == 1):
15                flat.extend(reversed(row))
16            else:
17                flat.extend(row)
18        
19        visited = set()
20        curr_q = deque()
21        next_q = deque()
22        curr_q.append(0)
23        count = 0
24        
25        while(curr_q or next_q):
26            count += 1
27            while(curr_q):
28                curr = curr_q.popleft()
29            
30                for i in range(1, 7):
31                    nextI = curr + i
32                    
33                    if nextI > len(flat) - 1:
34                        break
35                    if flat[nextI] != -1:
36                        nextI = flat[nextI] - 1
37                    if nextI == len(flat) - 1:
38                        return count
39                    if nextI not in visited:
40                        visited.add(nextI)
41                        next_q.append(nextI)
42            
43            curr_q = next_q
44            next_q = deque()
45        
46        return -1