# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        v = []
        if root:
            q.append(root)
        
        level = 0

        while len(q) > 0:
            
            print("level: ", level)

            v.append(q[-1].val)
            
            for n in range(len(q)):
                


                curr = q.popleft()
                
                print(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            
            level += 1
        
        return v
            






