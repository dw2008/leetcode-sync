# Last updated: 9/16/2026, 7:38:41 PM
1from collections import deque
2
3class Solution:
4    """
5    starting at beginword, do bfs and count the number of transformations to go to until the endWord
6    is reached. each neighbor of a word is the word with one letter changed that is still in wordList.
7    return the number of transformations required.
8    """
9    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
10        if(beginWord == endWord):
11            return 0
12        
13        visited = set()
14        curr_q = deque()
15        next_q = deque()
16        curr_q.append(beginWord)
17        wordSet = set(wordList)
18        count = 1
19        
20        while(curr_q):
21            while(curr_q):
22                curr = curr_q.popleft()
23                if(curr in visited):
24                    continue
25                visited.add(curr)
26                
27                for c in "qwertyuiopasdfghjklzxcvbnm":
28                    for i in range(0, len(curr)):
29                        temp = curr[:i] + c + curr[i+1:]
30                        if temp in wordSet and temp not in visited:
31                            if temp == endWord:
32                                return count + 1
33                            next_q.append(temp)
34                
35            curr_q = next_q
36            next_q = deque()
37            count += 1
38        
39        return 0