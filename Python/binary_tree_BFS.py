# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If the tree is empty, return an empty list
        
        result = []  # This will store the list of values at each level
        queue = deque([root])  # Initialize the queue with the root node
        
        while queue:
            level = []  # This will hold the values of the current level
            level_size = len(queue)  # Number of nodes in the current level
            
            for _ in range(level_size):  # Process all nodes in the current level
                node = queue.popleft()  # Remove the leftmost node from the queue
                level.append(node.val)  # Add its value to the level list
                
                # Add the left and right children to the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)  # Add the current level to the result
        
        return result


"""
Breadth-First Search (BFS) is a traversal technique that explores all nodes at a given depth (level) before moving to the next depth. It is particularly useful for operations that deal with levels, like returning nodes in level order or finding the shortest path in certain tree or graph problems.

Intuition
Imagine standing on top of the tree and looking at each level one by one, from left to right.
You process all nodes in the current level before moving to the next level.
BFS uses a queue (FIFO) to manage which nodes to process next, ensuring that we always process nodes in level order.
How It Works
Start at the root:

If the tree is empty, return an empty result.
Otherwise, add the root node to the queue.
Level by Level Traversal:

While the queue is not empty:
Determine the number of nodes at the current level (the size of the queue).
For each node at this level:
Remove it from the front of the queue.
Process its value.
Add its left and right children (if they exist) to the queue.
Result:

For each level, collect the processed values into a list.
Continue until all levels are processed.
"""
