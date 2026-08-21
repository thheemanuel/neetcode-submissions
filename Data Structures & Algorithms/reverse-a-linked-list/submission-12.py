# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None #eftersom current börjar på första noden, så är prev "null" eller utanför listan
        current = head #head är alltid första noden i en linkedlist

        while current: #medans current != nul
            next = current.next #denna säkerställer att det finns en nästa nod att hoppa till
            current.next = previous # flippa referensen
            previous = current #flytta upp previous till currs position
            current = next # flytta upp curr till nästa nod genom en pointer som vi satte i början
        return previous # efter hela loopen så returnerar vi previous efter som att det är det nya huvudet och curr blir ett steg utanför och blir "null" precis som prev va i början








        
