# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        list1 = []

        def inside(root):
            if not root:
                return None
            
            inside(root.left)
            list1.append(root.val)
            inside(root.right)

        inside(root)
        print(k)
        print(list1)
        k -= 1
        i = list1[k]
        
        return i






