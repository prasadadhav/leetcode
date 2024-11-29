from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Traverse to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the sublist between `left` and `right`
        curr = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp

        # Step 3: Connect the reversed sublist back to the main list
        prev.next.next = curr
        prev.next = next_node

        # Step 4: Return the modified head
        return dummy.next
                
        

sol = Solution()

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

"""