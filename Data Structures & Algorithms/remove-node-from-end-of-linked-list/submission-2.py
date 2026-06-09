# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and head.next is None:
            return None
        dummy_node = ListNode(-1)
        dummy_node.next = head 

        slow = head
        fast = head 

        counter = 1
        
        while counter <= n:
            fast = fast.next
            counter += 1 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
           
        slow.next = slow.next.next 

        return head
        
        

