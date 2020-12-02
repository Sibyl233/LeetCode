from typing import List

"""解法1：暴力法
- 时间复杂度：O(MN)
- 空间复杂度：O(1)
"""
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for column in row:
                if column==target:
                    return True
        return False

"""解法2：标志位法
- 时间复杂度：O(M+N)。最多循环M+N次。
- 空间复杂度：O(1)。指针使用常数大小额外空间。
"""
# class Solution:
#     def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
#         i, j = len(matrix) - 1, 0
#         while i >= 0 and j < len(matrix[0]):
#             if matrix[i][j] > target: i -= 1
#             elif matrix[i][j] < target: j += 1
#             else: return True
#         return False

if __name__=="__main__": 
    matrix = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
             ]
    # target = 5
    target = 20 
    print(Solution().findNumberIn2DArray(matrix, target)) # True(5) False(20)

