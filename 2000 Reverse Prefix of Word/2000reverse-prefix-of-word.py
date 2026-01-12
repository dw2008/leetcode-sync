class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #input: word with lowercase eng letters and ch lowercase eng letter
        #output: return word with reverse from 0 to index of first occurence of ch (inclusive) or just word if ch is not found
        #step 1: use a pointer to iterate through the string and see if ch is found
        #step 2a: when found, put reverse string from 0 to index of ch (inclusive) and then add on the rest of the string to a new string, then return new string
        #step 2b: if not found, return word
        #exceptions: i dont think there are any right now, since word must have a length therefore no null case
        for i in range(0, len(word)):
            if word[i] == ch:
                return word[0:i+1][::-1] + word[i+1:len(word)]
        
        return word