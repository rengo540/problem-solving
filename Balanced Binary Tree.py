# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    height =0
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return  self.balanced(root) != -1
    
    
    def balanced(self,root):
        
        if root is None :
            return 0 
        
        
        
        left = self.balanced(root.left)
        right = self.balanced(root.right)

        if left==-1 or right == -1 :
            return -1
        
        df = abs(left-right)
        if df>1 :
            return -1
        
        return max(right,left)+1



s = Solution()
