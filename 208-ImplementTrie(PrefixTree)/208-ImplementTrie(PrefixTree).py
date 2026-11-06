# Last updated: 11/6/2026, 5:31:01 PM
1class TrieNode:
2    def __init__(self, char = ""):
3        self.children = {}
4        self.is_end = False
5
6class Trie:
7
8    def __init__(self):
9        self.root = TrieNode()
10
11    def insert(self, word: str) -> None:
12        node = self.root
13        for char in word:
14            if char in node.children:
15                node = node.children[char]
16            else:
17                new_node = TrieNode(char)
18                node.children[char] = new_node
19                node = new_node
20        node.is_end = True
21
22    def search(self, word: str) -> bool:
23        node = self.root
24        for char in word:
25            if char not in node.children:
26                return False
27            node = node.children[char]
28        
29        return node.is_end
30        
31
32    def startsWith(self, prefix: str) -> bool:
33        node = self.root
34        for char in prefix:
35            if char not in node.children:
36                return False
37            node = node.children[char]
38        return True
39        
40
41# Your Trie object will be instantiated and called as such:
42# obj = Trie()
43# obj.insert(word)
44# param_2 = obj.search(word)
45# param_3 = obj.startsWith(prefix)