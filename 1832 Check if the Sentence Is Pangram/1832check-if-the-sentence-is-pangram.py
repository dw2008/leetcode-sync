class Solution:
    """
    use hashmap; for each letter in the sentence, put it in a hashmap. at the end, check if the hashmap
    includes each letter in alphabet by checking len == 26.
    """
    def checkIfPangram(self, sentence: str) -> bool:
        hash_map = {}
        
        for c in sentence:
            hash_map[c] = 1
            
        return len(hash_map) == 26