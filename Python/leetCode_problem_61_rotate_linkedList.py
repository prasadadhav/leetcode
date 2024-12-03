from typing import List

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge case: empty list or single node
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate the length of the list
        length = 1
        tail = head
        while tail.next:  # Traverse to find the tail and calculate length
            tail = tail.next
            length += 1

        # Step 2: Adjust k to be within the range of the list length
        k %= length
        if k == 0:  # No rotation needed
            return head

        # Step 3: Find the new tail (length - k - 1) and new head (length - k)
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next

        # Step 4: Rotate the list
        new_head = new_tail.next
        new_tail.next = None  # Break the list
        tail.next = head  # Link the old tail to the old head

        return new_head


sol = Solution()

"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
