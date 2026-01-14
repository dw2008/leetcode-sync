class Solution:
    #input: string s, integer k (s has definite length, s is all lowercase, k is within 1 and s.length)
    #output: max number of vowels of any substring of s w/ length k
    #strategy: use sliding window approach. have left and right pointers for the endpoints, and then make the first subarray starting with left = 0. calculate # of vowels in that array, then keep on moving window right, subtracting or adding to the # of vowels as needed.
    #edge cases: none that i can see currently
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        vowels = 0

        for i in range(k):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" :
                vowels += 1

        current = vowels
        for right in range(k, len(s)) :
            if s[right] == "a" or s[right] == "e" or s[right] == "i" or s[right] == "o" or s[right] == "u" :
                current += 1
            
            if s[left] == "a" or s[left] == "e" or s[left] == "i" or s[left] == "o" or s[left] == "u" :
                current -= 1
            
            vowels = max(current, vowels)
            left += 1
        
        return vowels