from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # Create a hashmap to store the index of each value in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(post_start, post_end, in_start, in_end):
            if post_start > post_end or in_start > in_end:
                return None
            
            # Root is the last element in postorder
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Get the index of the root in inorder
            root_index = inorder_map[root_val]
            
            # Calculate the size of the left subtree
            left_size = root_index - in_start
            
            # Recursively build the left and right subtrees
            root.left = helper(post_start, post_start + left_size - 1, in_start, root_index - 1)
            root.right = helper(post_start + left_size, post_end - 1, root_index + 1, in_end)
            
            return root
        
        return helper(0, len(postorder) - 1, 0, len(inorder) - 1)

sol = Solution()

"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
