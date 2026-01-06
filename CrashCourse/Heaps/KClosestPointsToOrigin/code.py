import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = math.sqrt(x * x + y * y)
            
            heapq.heappush(heap, (-distance, [x, y]))   # max heap implementaion

            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]

        # Time: N.log(k)
        # Space: O(k)
            
