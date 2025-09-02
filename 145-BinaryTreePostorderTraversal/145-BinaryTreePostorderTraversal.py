# Last updated: 9/2/2025, 1:43:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        current=root
        result=[]
        last_visited=None
        while stack or current:
            if current:
                stack.append(current)
                current=current.left
            else:
                node=stack[-1]
                if node.right and node.right!=last_visited:
                    current=node.right
                else:
                    result.append(node.val)
                    last_visited=stack.pop()
        return result

        