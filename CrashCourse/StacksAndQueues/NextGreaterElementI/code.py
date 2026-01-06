class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
    
        for num2 in nums2:
            while stack and stack[-1] < num2:
                hashmap[stack.pop()] = num2
        
            stack.append(num2) 

        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap.get(num1, -1) for num1 in nums1]
        
