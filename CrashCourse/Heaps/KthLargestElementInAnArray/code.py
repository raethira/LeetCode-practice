import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)   # min heap implementation
            
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

        # Time: N.log(k)
        # Space: O(k)
