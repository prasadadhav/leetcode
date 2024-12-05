# Recursive solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Base case: If the node is null, return an empty list
        if not root:
            return []
        
        # Inorder: left -> root -> right
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        current = root
        
        while stack or current:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left
            
            # Process the node at the top of the stack
            current = stack.pop()
            result.append(current.val)
            
            # Move to the right subtree
            current = current.right
        
        return result


"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

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
