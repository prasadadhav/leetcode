from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Helper function to reverse a portion of the list
        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the end of the current group
            group_end = group_prev
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next

            # Save the next group's start
            next_group_start = group_end.next

            # Reverse the current group
            group_start = group_prev.next
            group_end.next = None
            reversed_group = reverse(group_start, None)

            # Connect the reversed group to the rest of the list
            group_prev.next = reversed_group
            group_start.next = next_group_start

            # Move `group_prev` to the end of the current group
            group_prev = group_start

        

sol = Solution()

"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""
