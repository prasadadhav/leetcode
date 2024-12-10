from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Function to compute the height of the leftmost path
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        # Function to compute the height of the rightmost path
        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        left_height = get_left_height(root)
        right_height = get_right_height(root)

        # If left and right heights are equal, the tree is a full binary tree
        if left_height == right_height:
            return (1 << left_height) - 1  # 2^h - 1 nodes in a full binary tree

        # Otherwise, recurse into left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

sol = Solution()

"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
