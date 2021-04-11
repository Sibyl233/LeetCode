# 只有B为空时才把A的所有元素倾倒进B中，这样顺序就不会乱了
class CQueue:

    def __init__(self):
        self.A = []
        self.B = []


    def appendTail(self, value: int) -> None:
        self.A.append(value)


    def deleteHead(self) -> int:
        if not self.B:
            if not self.A:
                return -1
            else:
                while self.A:
                    self.B.append(self.A.pop())
        
        return self.B.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()