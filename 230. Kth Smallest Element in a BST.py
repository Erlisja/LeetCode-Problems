"""
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
                   5
                 /   \
                3     6
               / \
              2   4
             /      
            1  

we need to do a in order-trasversal to visit all the nodes 
a helper function will make sure we visit left and then right subtrees to check if we reached the k-th position          
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    self.position = 0
    self.value = 0
    
    # helper function
    def inOrder (currNode):
        # Base Case
        if currNode == None:
            return
        #Check left subtree
        inOrder(currNode.left)
        self.position +=1
        if self.position == k:
            value = currNode.val
            return 
        
        # Check right subtree
        inOrder(currNode.right)

    inOrder(root)
    return self.value


