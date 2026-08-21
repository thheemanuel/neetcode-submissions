# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        outer = []
        inner = []

        if root:
            q.append(root)
        
        level = 0

        while len(q) > 0:

            print('level: ', level)

            for n in range(len(q)):

                curr = q.popleft()
                inner.append(curr.val)
                print(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            outer.append(inner)
            temp = []
            inner = temp
            level += 1
        
        return outer





