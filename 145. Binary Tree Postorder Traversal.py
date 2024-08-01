"""
     1
  2    3
 4 5  6 7

4,5,2,6,7,3,1

1. base case-> if root is none, return an empty list
2. traverse the left subtree recursively and add its value to the array
3.traverse the right subtree recursively and add its value to the array
4. add the current's node value to the list
"""

def postorderTraversal(self,root: Optional[TreeNode])->List[int]:
    # create a helper function
    def postorder(node):
        # base case
        if not node:
            return []
        #traverse the left subtree and add its value to the array
        left = postorder(node.left)
        # traverse the right subtree
        right = postorder(node.right)
        # traverse center
        center = [node.val]
        return left + right + center
    
    return postorder(root)
    