from typing import List

"""解法1：二次遍历
- 时间复杂度：O(2*N^2)
- 空间复杂度：O(1)
"""
# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
#         rows = len(A)
#         cols = len(A[0])
#         for row in range(rows):
#             A[row] = A[row][::-1]
#             for col in range(cols):
#                 A[row][col] ^= 1
#         return A

"""解法2：一次遍历
- 时间复杂度：O(N^2)
- 空间复杂度：O(1)
"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        for i in range(N):
            for j in range((N + 1)//2):
                A[i][j], A[i][N - 1 - j] = 1 - A[i][N - 1 - j], 1- A[i][j] # a,b = 1-b,1-a
        return A

if __name__ == "__main__":
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(Solution().flipAndInvertImage(A)) # [[1,0,0],[0,1,0],[1,1,1]]