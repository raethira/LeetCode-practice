class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        def binarySearchRightIndex(arr, target):
            left = 0
            right = len(arr)

            while left < right:
                mid = (left + right) >> 1
                
                if(arr[mid] > target):
                    right = mid
                
                else:
                    left = mid + 1
                
            return left

        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        answer = []

        for q in queries:
            answer.append(binarySearchRightIndex(nums, q))

        return answer
