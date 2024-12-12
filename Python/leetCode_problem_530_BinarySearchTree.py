from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None  # Store the value of the previous node in in-order traversal
        self.min_diff = float('inf')  # Initialize the minimum difference to infinity

        def in_order(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order(node.left)

            # Process the current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev))
            self.prev = node.val  # Update the previous node value

            # Traverse the right subtree
            in_order(node.right)

        in_order(root)  # Start the in-order traversal
        return self.min_diff



sol = Solution()

"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
