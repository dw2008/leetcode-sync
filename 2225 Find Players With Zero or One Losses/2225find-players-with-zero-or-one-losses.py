class Solution:
    """
    using hashmap of each player and the amount of times they lose; for each winner/loser pair in  
    matches, put the winner in the hashmap (0 by default) and add 1 loss to the loser in the hashmap.
    when done with every pair, put each player with 0 losses and 1 loss in two subarrays within an
    array and return the array.
    """
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()
        for pair in matches:
            losses[pair[0]] = losses.get(pair[0], 0)
            losses[pair[1]] = losses.get(pair[1], 0) + 1
        
        answer = [[],[]]
        for player, n in losses.items():
            if n == 0:
                answer[0].append(player)
            if n == 1:
                answer[1].append(player)
        
        answer[0].sort()
        answer[1].sort()
        return answer