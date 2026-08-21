# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head

        while current:
            next = current.next #denna säkerställer att det finns en nästa nod att hoppa till
            current.next = previous # efter att man har flippat alla referenser 
            previous = current
            current = next
        return previous








        
