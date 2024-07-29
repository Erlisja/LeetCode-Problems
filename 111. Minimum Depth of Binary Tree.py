"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

def minDepth(self, root: Optional[TreeNode]) -> int:
    # Base case
    if root == None:
        return 0
    #if there is only left subtree
    if root.left:
        return self.minDepth(root.left)+1
    #if there is only right subtree
    elif root.right:
        return self.minDepth(root.right)+1
    else:
        # both subtrees exist
        return min (minDepth(root.left),minDepth(root.right))+1