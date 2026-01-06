class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()
        max_weight = 5000
        count = 0

        for apple in weight:
            if max_weight - apple >= 0:
                max_weight -= apple
                count += 1

        return count
