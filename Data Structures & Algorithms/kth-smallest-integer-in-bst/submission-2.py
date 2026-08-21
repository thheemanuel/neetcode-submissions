# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        list1 = [] #skapa en lista som ska ha alla värden i storleksordning

        def inside(root): #hjälpfunktion som går igenom hela trädet och lägger till nodernas värde i storleksordning i listan, från minst till sist.
            if not root:
                return None
            
            inside(root.left)
            list1.append(root.val)
            inside(root.right)

        inside(root) #kalla på hjälpfunktionen så att listan innehåller värdena i listan i storleksordning
        k -= 1 #eftersom att listan räknar från 0 behöver vi ändra k till ett värde mindre
        i = list1[k] #sätt i till "kth" minsta värdet i listan
        
        return i #returnera 






