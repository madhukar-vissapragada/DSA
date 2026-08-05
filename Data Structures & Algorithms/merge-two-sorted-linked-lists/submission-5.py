# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = ListNode(-1)
        temp_head = temp_node

        i = list1 
        j = list2 

        while i and j:
            if i.val <= j.val:
                temp_node.next = i
                temp_node = temp_node.next 
                i = i.next 
            else:
                temp_node.next = j
                temp_node = temp_node.next 
                j = j.next
        
        if i:
            temp_node.next = i 
        
        if j:
            temp_node.next = j 
        
        return temp_head.next 

    