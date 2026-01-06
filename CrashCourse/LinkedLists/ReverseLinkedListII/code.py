# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)            # Initialize a dummy node to simplify edge cases 
                                       # and connect it to the head of the linked list.

                                       # Create a dummy node with a value of 0 and set its next pointer #            head  of the linked list. This dummy node helps in handling the case when left is 1, at line 21.

        dummy.next = head
        prev = dummy

        # Step 1: Move prev to the node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Set pointers for the reversal
        headOfSubList = prev.next
        curr = headOfSubList
        prev_node = prev

        # Step 3: Reverse between left and right
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        # Step 4: Reconnect the reversed sublist
        prev.next = prev_node              # prev_node is the new head of the reversed sublist
        headOfSubList.next = curr          # connect tail of reversed sublist to remaining list

        return dummy.next

        # Another algorithm using Head-Insertion Technique - code from:- https://leetcode.com/problems/reverse-linked-list-ii/solutions/5418381/video-simple-solution/
            
