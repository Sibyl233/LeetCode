from typing import List

"""解法：遍历
- 时间复杂度：O(mn)
- 空间复杂度：O(1)
"""
# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         for i in range(len(matrix) - 1):
#             for j in range(len(matrix[0]) - 1):
#                 if matrix[i][j] != matrix[i + 1][j + 1]:
#                     return False
#         return True

# 切片
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(Solution().isToeplitzMatrix(matrix)) # True
