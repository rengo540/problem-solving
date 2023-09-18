# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    diameter = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dia(root)
        return self.diameter
        
    def dia (self,root):
         
        if root is None :
            return -1 
        
        from_right = self.dia(root.right)+1
        from_left = self.dia(root.left)+1
        self.diameter = max(from_right+from_left,self.diameter)
        if from_right>= from_left:
            
            return from_right
        else:
            return from_left



root =                                  TreeNode(1,
                left=TreeNode(2,
        left=TreeNode(4),right=TreeNode(5))                 ,right=TreeNode(3))


s = Solution()
res=s.diameterOfBinaryTree(root)
print(s.diameter)