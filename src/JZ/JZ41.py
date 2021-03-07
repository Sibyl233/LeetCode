from heapq import *

"""解法：堆
- 时间复杂度：查找 O(1)；添加 O(logn)
- 空间复杂度：O(n)
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] #小顶堆，保存较大的一半
        self.B = [] #大顶堆，保存较小的一半


    def addNum(self, num: int) -> None:
        # 当n为奇数
        if len(self.A) != len(self.B): 
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        # 当n为偶数
        else:                          
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()