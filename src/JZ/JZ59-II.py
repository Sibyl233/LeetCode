import collections
class MaxQueue:

    def __init__(self):
        self.A = collections.deque()
        self.B = collections.deque()


    def max_value(self) -> int:
        if not self.B:
            return -1
        else:
            return self.B[0]


    def push_back(self, value: int) -> None:
        while self.B and value > self.B[-1]:
            self.B.pop()
        self.B.append(value)
        self.A.append(value)

    def pop_front(self) -> int:
        if not self.A:
            return -1
        res = self.A.popleft()
        if res == self.B[0]:
            self.B.popleft()
        return res



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()


