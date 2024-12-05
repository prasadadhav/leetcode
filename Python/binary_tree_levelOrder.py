# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        from typing import List, Optional
        
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the current node
                current_level.append(node.val)  # Add its value to the current level

                if node.left:  # Enqueue left child if it exists
                    queue.append(node.left)
                if node.right:  # Enqueue right child if it exists
                    queue.append(node.right)

            result.append(current_level)  # Add the current level to the result

        return result


"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
