from typing import List

"""解法：模拟
- 时间复杂度：O(mn)
- 空间复杂度：O(1)
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        res = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    print(Solution().transpose(matrix)) # [[1,4],[2,5],[3,6]]
