# Last updated: 9/30/2026, 5:45:32 PM
1class Solution:
2    """
3    this problem can be solved using a combination of greedy + binary search. let us have a sweetness
4    s that represents the minimum sweetness for a piece. we can start that sweetness at the (minimum
5    possble sweetness + the maximum possible sweetness) // 2. we can then sum each part of the choco
6    bar starting from the left, adding until we get a piece that is >= minimum sweetness, then moving
7    on to the next piece. if we reach the end without giving all pieces, then we know that the min
8    sweetness is not valid, and we have to move right = s-1, and vice versa if we do not reach the end
9    before giving all pieces. we can return the maximum valid sweetness that we can keep trakc of.
10    """
11    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
12        your_piece = -1
13        left = min(sweetness) #min possible sweetness for a cut
14        max_sweet = sum(sweetness) // (k+1) #this is the max possible sweetness for a cut
15        right = max_sweet
16        
17        while left <= right:
18            mid = (left + right)//2
19            chunk_counter = 0
20            index = 0
21            current_sweet = 0
22            your_current_piece = max_sweet #want to compare to find the smallest piece made from this
23            
24            while (chunk_counter < k+1 and index < len(sweetness)): #go thru the bar until a condition
25                current_sweet += sweetness[index]
26                if(current_sweet >= mid):
27                    chunk_counter += 1
28                    your_current_piece = min(your_current_piece, current_sweet) #you take smallest
29                    current_sweet = 0
30                index += 1
31            
32            if chunk_counter < k+1:
33                right = mid-1
34            
35            else:
36                your_piece = max(your_current_piece, your_piece) #update your piece if its bigger
37                left = mid+1
38        
39        return your_piece