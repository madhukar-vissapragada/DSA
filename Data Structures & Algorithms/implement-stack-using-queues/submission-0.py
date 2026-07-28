class MyStack:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        item = self.queue.pop(0)
        return item

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0