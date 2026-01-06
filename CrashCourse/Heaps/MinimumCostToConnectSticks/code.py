import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_cost = 0
        heapq.heapify(sticks)   # N.log(N)

        while len(sticks) > 1:
            min_element_x = heapq.heappop(sticks)        
            min_element_y = heapq.heappop(sticks)        
            heapq.heappush(sticks, min_element_x + min_element_y)
            min_cost = min_cost + min_element_x + min_element_y

        return min_cost

