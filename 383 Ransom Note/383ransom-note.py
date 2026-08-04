class Solution:
    """
    use a hashmap to count the number of occurences of each letter in magazine, then decrease value
    by 1 for each occurence in ransomnote and return true if there are no negative values and false if 
    there are (or if there are ransomnote letters not in magazine)
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        
        for letter in ransomNote:
            if (letter not in letters) or (letters.get(letter) == 0):
                return False
            letters[letter] -= 1
        
        return True