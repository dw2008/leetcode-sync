# Last updated: 9/13/2026, 6:19:38 PM
1from collections import deque
2
3class Solution:
4    """
5    perform BFS on the startGene until reaching endGene; start at start and then try to switch each
6    character with another character and see if its in the bank and not visited, if so add into a
7    queue to then continue, keep doing until mutated or return -1 if not able to do so
8    """
9    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
10        if(startGene == endGene):
11            return 0
12        
13        if(not bank or endGene not in bank):
14            return -1
15        
16        curr_q = deque()
17        next_q = deque()
18        curr_q.append(startGene)
19        visited = set()
20        count = 0
21        
22        while(curr_q):
23            while(curr_q):
24                curr = curr_q.popleft()
25                visited.add(curr)
26            
27                for code in "GACT":
28                    for i in range(0, len(startGene)):
29                        newGenes = curr[:i] + code + curr[i+1:]
30                        if(newGenes == endGene):
31                            return count + 1
32                        if(newGenes not in visited and newGenes in bank):
33                            next_q.append(newGenes)
34
35            curr_q = next_q
36            next_q = deque()
37            count += 1
38        
39        return -1