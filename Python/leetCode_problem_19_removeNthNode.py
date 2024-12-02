from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: Initialize two pointers
        fast = dummy
        slow = dummy

        # Step 3: Move `fast` pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Step 4: Move `fast` and `slow` together until `fast` reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Step 5: Remove the nth node
        slow.next = slow.next.next

        # Step 6: Return the modified list
        return dummy.next


sol = Solution()

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""
