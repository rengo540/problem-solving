# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return False 
        
        if root.val == subRoot.val:
            if self.isSame(root,subRoot):
                return True
        
        left= self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        
        return left or right
        
        
        

    def isSame(self,p,q):
        
        if p is None and q is None :
            return True
        elif p is None:
            return False
        elif q is None:
            return False

        left=self.isSame(p.left,q.left)
        right=self.isSame(p.right,q.right)
        if left and right:
            return p.val == q.val
        
        return False
    
s = Solution()

p = TreeNode(4)
p.left=TreeNode(1)
p.right=TreeNode(2)
p.right.left=TreeNode(0)

q = TreeNode(4)
q.left=TreeNode(1)
q.right=TreeNode(2)



print(s.isSame(p,q))