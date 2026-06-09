class ListNode: 
    def __init__(self,value):
        self.val = value 
        self.prev = None 
        self.next = None 


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = 0
        self.max_size = k
        self.head = None 
        self.tail = None
        

    def enQueue(self, value: int) -> bool:
        if self.k == self.max_size:
            return False

        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.k += 1
        
        return True

    def deQueue(self) -> bool:
        if self.tail == None:
            return False 
        
        node_to_delete = self.tail
        self.tail = node_to_delete.prev
        if self.tail:
            self.tail.next = None
        del node_to_delete
        self.k -= 1
        return True

        

    def Front(self) -> int:
        if self.tail:
            return self.tail.val
        return -1        

    def Rear(self) -> int:
        if self.head:
            return self.head.val
        return -1 
        

    def isEmpty(self) -> bool:
        return self.k == 0
        

    def isFull(self) -> bool:
        return self.k == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()