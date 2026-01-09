class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []

        for char in s:
            if char.isalpha():
                letters.append(char)

        res = []
        for char in s:
            if char.isalpha():
                res.append(letters.pop())
            else:
                res.append(char)
        
        return "".join(res)