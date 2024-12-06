from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        # Process right subtree first
        self.flatten(root.right)

        # Process left subtree
        self.flatten(root.left)

        # Set the current node's right to prev and left to null
        root.right = self.prev
        root.left = None

        # Update prev to current node
        self.prev = root

sol = Solution()

"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?


Approach: Reverse Post-order Traversal :
This approach processes the tree in reverse post-order (right → left → root). It ensures that we directly link the nodes in the desired "linked list" order.

Algorithm :
Use a pointer prev to track the last processed node in the flattened list.
Traverse the tree in reverse post-order:
Process the right subtree.
Process the left subtree.
Set the current node’s right child to prev and its left child to null.
Update prev to the current node.
Repeat until the entire tree is processed.
This method avoids extra space since it modifies the tree in place.

Algorithm Complexity :
Time Complexity: O(n), where n is the number of nodes (each node is visited once).
Space Complexity: O(h), where h is the height of the tree (call stack for recursion).
"""
