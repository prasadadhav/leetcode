from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Step 1: Create two dummy nodes
        less_head = ListNode(0)
        greater_head = ListNode(0)

        # Step 2: Initialize pointers for the two lists
        less_tail = less_head
        greater_tail = greater_head

        # Step 3: Traverse the original list
        while head:
            if head.val < x:
                # Add node to the 'less' list
                less_tail.next = head
                less_tail = less_tail.next
            else:
                # Add node to the 'greater' list
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next

        # Step 4: Connect the two lists
        less_tail.next = greater_head.next
        greater_tail.next = None  # Ensure the end of the list points to None

        # Step 5: Return the new head
        return less_head.next

sol = Solution()

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
