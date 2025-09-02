# Last updated: 9/2/2025, 1:43:01 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
    def preorder(self,root,result):
        if root!=None:
            result.append(root.val)
            self.preorder(root.left,result)
            self.preorder(root.right,result)

    def preorderTraversal(self, root):
        res=[]
        self.preorder(root,res)
        return res