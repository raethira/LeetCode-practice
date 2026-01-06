class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        def check(x):
            cur_sweetness = 0
            people_with_chocolate = 0
            
            # Start assigning chunks to the current person.
            for s in sweetness:
                cur_sweetness += s
                
                # If the total sweetness is no less than mid, this means we can break off
                # the current piece and move on to assigning chunks to the next person.
                if cur_sweetness >= x:
                    people_with_chocolate += 1
                    cur_sweetness = 0
            
            return people_with_chocolate >= k + 1

        
        number_of_people = k + 1
        left = min(sweetness)  # or 1, also works
        right = sum(sweetness) // number_of_people

        while left <= right:
            mid = (left + right) // 2
            
            if check(mid):
                left = mid + 1
            
            else:
                right = mid - 1

        return right

        # Solution copied from Editorial section: https://leetcode.com/problems/divide-chocolate/editorial/
