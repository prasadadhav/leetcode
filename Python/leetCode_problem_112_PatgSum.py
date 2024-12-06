from typing import List

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        # Subtract current node's value from targetSum
        targetSum -= root.val
        
        # Check if it's a leaf node and targetSum becomes zero
        if not root.left and not root.right:
            return targetSum == 0
        
        # Recursively check left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
#BFS
from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, targetSum - root.val)])
        
        while queue:
            node, curr_sum = queue.popleft()
            
            # Check if the current node is a leaf and its sum is zero
            if not node.left and not node.right and curr_sum == 0:
                return True
            
            # Add left child to queue if exists
            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
            
            # Add right child to queue if exists
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))
        
        return False

sol = Solution()

"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

Intuition :
The problem requires checking if there is a root-to-leaf path in a binary tree whose nodes sum up to a given targetSum. A leaf node is defined as a node with no children. We can solve this problem using Depth-First Search (DFS) or Breadth-First Search (BFS).

Approach :
Depth-First Search (DFS) Recursive:

Traverse the tree in a depth-first manner.
At each node, subtract its value from the current targetSum.
If you reach a leaf node and the remaining targetSum becomes zero, return True.
If no valid path is found, return False.
Breadth-First Search (BFS) Iterative:

Use a queue to traverse the tree level by level.
Keep track of the cumulative sum along the path.
If a leaf node is reached and its cumulative sum equals targetSum, return True.
If all nodes are processed and no valid path is found, return False.
Algorithm. :
DFS Recursive :
If the tree is empty (root == None), return False.
Subtract the current node’s value from the targetSum.
If the node is a leaf and the remaining targetSum equals 0, return True.
Recursively call the function for left and right subtrees.
Return True if either subtree returns True.
"""
