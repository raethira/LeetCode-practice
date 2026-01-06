class Solution:
    def countElements(self, arr: List[int]) -> int:
        countMap = {}
        answer = 0
        
        for elem in arr:
            if elem in countMap:
                countMap[elem] += 1
            else:
                countMap[elem] = 1

            if elem + 1 in countMap:
                answer += 1
            if elem - 1 in countMap and countMap[elem] == 1:
                answer += countMap[elem - 1]
            
        return answer
