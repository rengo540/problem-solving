# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

    def same(self,p,q):
        
        if p is None and q is None :
            return True
        elif p is None:
            return False
        elif q is None:
            return False

        left=self.same(p.left,q.left)
        right=self.same(p.right,q.right)
        if left and right:
            return p.val == q.val
        
        return False