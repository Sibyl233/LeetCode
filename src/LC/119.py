from typing import List

"""解法1_1：找规律
- 时间复杂度：O(numRows^2)
- 空间复杂度：O(1)。不考虑返回值的空间占用。
"""
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         res = []
#         for i in range(rowIndex+1):
#             res.append([1] * (i + 1))
#             for j in range(1, i):
#                 res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
#         return res[rowIndex]

"""解法1_2：找规律+优化。参考LC62。
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        cur = [1]
        for i in range(rowIndex+1):
            for j in range(1, i):
                cur[j] = pre[j - 1] + pre[j]
            pre = cur[:]
            cur.append(1)
        return pre

if __name__ == "__main__":
    rowIndex = 3
    print(Solution().getRow(rowIndex))