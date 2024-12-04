from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        from collections import deque
        from typing import List, Optional
        
        if not root:
            return 0

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

        return len(result)
        
root = [3,9,20,null,null,15,7]
sol = Solution()
print(sol.maxDepth(root))

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
