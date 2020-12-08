from typing import List

"""解法1：找规律
- 时间复杂度：O(numRows^2)
- 空间复杂度：O(1)。不考虑返回值的空间占用。
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res

"""解法2：找规律
"""


if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
