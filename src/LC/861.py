from typing import List

"""解法：贪心
- 时间复杂度：O(mn)
- 空间复杂度：O(1)
"""
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        res = m

        for j in range(1, n):
            res <<= 1                                      # 可以理解为在某一列的数字确定后通过左移运算符计算其真实值。以第一列为例，一开始是3（3个1），经过3次循环后，变为24.
            s = sum([A[i][j] ^ A[i][0] for i in range(m)]) # 对应步骤1
            res += max(s, m - s)                           # 对应步骤2
        
        return res

if __name__ == "__main__":
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(Solution().matrixScore(A)) # 39