class Solution:
    """
    using hashmap; put each letter in balloon as a key in a hashmap, increment value by 1 each time
    a letter is mentioned, then go through the dictionary and seeing if balloon can be made
    and then dividing the corresponding amoutn of letters from each letter and using the smallest
    value to determine how many balloons
    b: 1, a: 1, l: 2, o: 2, n: 1
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        letters['b'] = 0
        letters['a'] = 0
        letters['l'] = 0
        letters['o'] = 0
        letters['n'] = 0
        
        for i in range(len(text)):
            if text[i] == 'b':
                letters['b'] = letters.get('b') + 1
            elif text[i] == 'a':
                letters['a'] = letters.get('a') + 1
            elif text[i] == 'l':
                letters['l'] = letters.get('l') + 1
            elif text[i] == 'o':
                letters['o'] = letters.get('o') + 1
            elif text[i] == 'n':
                letters['n'] = letters.get('n') + 1
        
        num = float('inf')
        for letter, val in letters.items():
            if letter == 'b' or letter == 'a' or letter == 'n':
                num = min(num, val)
            else:
                num = min(num, val//2)
        return num