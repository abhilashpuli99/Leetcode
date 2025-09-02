# Last updated: 9/2/2025, 1:43:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result=[]
        q=deque()
        if not root:
            return 0
        q.append(root)
        while q:
            level=len(q)
            sublevel=[]
            while level:
                node=q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sublevel.append(node.val)
                level-=1  
            result.append(sublevel)
        return len(result)
        