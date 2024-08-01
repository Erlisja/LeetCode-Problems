"""
     1
  2    3
 4 5  6 7

1,2,4,5,3,6,7

1. base case-> if root is none, return an empty list
2. add the current's node value to the list
3. traverse the left subtree recursively and add its value to the array
4.traverse the right subtree recursively and add its value to the array

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node):
            # base case:
            if not node:
                return []
            result = [node.val]
            left = preorder(node.left)
            right = preorder(node.right)
            return result + left + right
        return preorder(root)
