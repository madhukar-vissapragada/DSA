# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()
        current = head 

        while current:
            if current in hash_set:
                return True 
            hash_set.add(current)
            current = current.next 
    
        return False 