# Recursive solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Base case: If the node is null, return an empty list
        if not root:
            return []
        
        # Preorder: root -> left -> right
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# iterative solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack, result = [root], []
        
        while stack:
            # Pop the top of the stack
            node = stack.pop()
            
            # Visit the node
            result.append(node.val)
            
            # Push right child first (to be processed later)
            if node.right:
                stack.append(node.right)
            
            # Push left child (to be processed next)
            if node.left:
                stack.append(node.left)
        
        return result




"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
