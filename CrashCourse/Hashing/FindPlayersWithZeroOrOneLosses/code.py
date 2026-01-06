class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)
        answer1 = []
        
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        
        for loser, lost in losers.items():
            if lost == 1:
                answer1.append(loser)
        
        return [sorted(winners - set(losers)), sorted(answer1)]
        
