# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode() #creating a dummynode to begin the new linked list
        tail = dummyNode #assigning "tail" to the dummynode, tail will eventually be the last node in the list

        while list1 and list2: #while both list1 and list2 != null
            if list1.val < list2.val: #if the value of the first node in list1 is less than the value of the first node in list 2
                tail.next = list1 #then add the node to the new list (the merged sorted list)
                list1 = list1.next #then, move the head of list1 to the next node
            else:
                tail.next = list2 #else assign the list2 node to be the one that gets added to the new merged list
                list2 = list2.next #move the head of the list to the next node
            tail = tail.next #move tail so that tail is the last node in the new merged list and ready to add another one to the merged list

            #this if statement covers the case where one list stops (is shorter) than the other, the solution then is just to add (since they are sorted) the remainder of the list to the new merged list
        if list1: #if list1 != null
            tail.next = list1 #add the remainder of list1 after the tail
        elif list2: #if list2 != null
            tail.next = list2 #add the remainder of list2 after the tail
        
        return dummyNode.next #return the new merged list, which is after the dummy node. therefore the "dummyNode.next"












