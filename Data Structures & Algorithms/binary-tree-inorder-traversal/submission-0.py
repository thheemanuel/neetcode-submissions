# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        listbruh = []
        
        def inside(root):
            if not root:
                return
        
            inside(root.left)
            listbruh.append(root.val)
            inside(root.right)
        
        inside(root)
        return listbruh





