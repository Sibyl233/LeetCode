class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.a) > 1:
            self.b.append(self.a.pop())
        element = self.a.pop()
        while len(self.b) > 0:
            self.a.append(self.b.pop())
        return element

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.a) > 1:
            self.b.append(self.a.pop())
        element = self.a.pop()
        self.b.append(element)
        while len(self.b) > 0:
            self.a.append(self.b.pop())
        return element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.a) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()