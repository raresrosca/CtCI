# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: #pylint: disable=undefined-variable
        queue = [root]
        
        while queue:
            length = len(queue)
            i = 0
            j = length - 1
            
            while i < j:
                if queue[i] is None and queue[j] is None:
                    i += 1
                    j -= 1
                elif queue[i] is None or queue[j] is None:
                    return False
                else:
                    if queue[i].val != queue[j].val:
                        return False
                    else:
                        i += 1
                        j -= 1
            
            while length:
                current = queue.pop(0)
                if current is not None:
                    queue.append(current.left)
                    queue.append(current.right)
                length -= 1
                
        return True
    