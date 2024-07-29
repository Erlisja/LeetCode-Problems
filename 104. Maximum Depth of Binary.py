"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

def maxDepth(self, root: Optional[TreeNode]) -> int:
    #base case
    if root is None:
        return 0
    # recursively find the depth of right and left subtrees    
    return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
