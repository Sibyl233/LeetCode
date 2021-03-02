from typing import List

"""解法1：一维前缀和
- 时间复杂度：初始化 O(mn)，每次检索时间O(m)
- 空间复杂度：O(mn)
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.preSum = [[0] * (n + 1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.preSum[i][j + 1] = self.preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.preSum[i][col2 + 1] - self.preSum[i][col1] for i in range(row1, row2 + 1))

"""解法2：二维前缀和
- 时间复杂度：初始化 O(mn)，每次检索时间O(1)
- 空间复杂度：O(mn)
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.preSum = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                self.preSum[i + 1][j + 1] = self.preSum[i+1][j] + self.preSum[i][j+1] - self.preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] - self.preSum[row2+1][col1] - self.preSum[row1][col2+1] + self.preSum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
