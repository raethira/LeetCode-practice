import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        while k > 0:
            max_element = -heapq.heappop(piles)
            max_element = math.ceil(max_element / 2)           # Bug in question- should be "keep", instead of "remove".
            heapq.heappush(piles, -max_element)         
            k -= 1

        return -sum(piles)
