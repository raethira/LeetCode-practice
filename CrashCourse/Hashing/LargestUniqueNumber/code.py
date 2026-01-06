class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        answer = -1
        frequencyMap = Counter(nums)
            
        for num, frequency in frequencyMap.items():
            if answer < num and frequency == 1:
                answer = num
            
        return answer
