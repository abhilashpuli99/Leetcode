# Last updated: 9/2/2025, 1:43:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""def levelOrder(root):
        result=[]
        rightview=[]
        q=deque()
        if not root:
            return result
        q.append(root)
        while q:
            level=len(q)
            sublevel=[]
            while level:
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    sublevel.append(node.val)
                else:
                    q.append(None)
                level-=1
            result.append(sublevel)
        return result"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
         
        