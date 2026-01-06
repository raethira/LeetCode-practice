import heapq 

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        frequenciesMap = Counter(arr)
        frequencies = [-value for value in frequenciesMap.values()]

        heapq.heapify(frequencies)
        n = len(arr)
        setsize = m = 0

        while frequencies:
            m += heapq.heappop(frequencies)
            setsize += 1
            if -m >= n / 2:
                return setsize

        return setsize
