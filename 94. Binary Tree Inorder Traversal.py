"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""




def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # create a helper function
        def inorder(node):
            if node == None:
                return []
            #traverse left subtree
            left = inorder(node.left)
            # traverse root node
            center = [node.val]
            # traverse right subtree
            right = inorder(node.right)
            # combine the results
            return left + center + right
        return inorder(root)