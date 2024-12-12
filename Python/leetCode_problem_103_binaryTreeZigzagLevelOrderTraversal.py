from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return empty list if tree is empty
        
        result = []
        queue = deque([root])  # Initialize queue with root node
        left_to_right = True  # Direction flag
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()  # Remove node from the front of the queue
                if left_to_right:
                    level.append(node.val)  # Append in left-to-right order
                else:
                    level.insert(0, node.val)  # Insert at the beginning for right-to-left order
                
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)  # Add current level to the result
            left_to_right = not left_to_right  # Flip direction
        
        return result


sol = Solution()

"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
