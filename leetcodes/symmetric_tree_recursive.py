# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: #pylint: disable=undefined-variable
        if root == None:
            return True
        
        return isMirror(root.left, root.right)
        
    
def isMirror(left, right):
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    else:
        if left.val != right.val:
            return False
        else:
            a = isMirror(left.left, right.right)
            b = isMirror(left.right, right.left)
            return (a and b)
        
            
            
        