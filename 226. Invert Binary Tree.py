"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
     2            2
    / \          / \
   1   3        3   1

Example 3:
Input: root = []
Output: []

"""
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # base case
    if root == None:
        return None
    
    # swap left and right subtress recursively
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root