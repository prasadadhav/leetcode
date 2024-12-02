from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: Use two pointers: prev and curr
        prev = dummy  # Points to the last node in the result list
        curr = head   # Iterates through the original list

        while curr:
            # Step 3: Check for duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Remove the duplicates by adjusting the `next` pointer of prev
                prev.next = curr.next
            else:
                # If no duplicates, move prev to curr
                prev = curr
            
            # Move curr to the next node
            curr = curr.next

        # Step 4: Return the head of the modified list
        return dummy.next


sol = Solution()

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
