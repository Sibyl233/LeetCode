from typing import List

"""解法1_1：动态规划(必须画表格)
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def constructArr(self, a: List[int]) -> List[int]:
#         n = len(a)
#         # L 表示 a[i] 左边的乘积， R 表示 a[i] 右边的乘积
#         L, R = [1] * n, [1] * n
#         for i in range(1, n):
#             L[i] = L[i - 1] * a[i - 1]
#         for i in range(n - 2, -1, -1):
#             R[i] = R[i + 1] * a[i + 1]
#         return [L[i] * R[i] for i in range(n)]

"""解法1_2：优化的动态规划(必须画表格)
- 时间复杂度：O(n)
- 空间复杂度：O(1)。b 作为返回值不计。
"""
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        b = [1] * n
        tmp = 1
        for i in range(1, n):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(n - 2, -1, -1):
            tmp *= a[i+1]
            b[i] = b[i] * tmp
        return b

if __name__ == "__main__":
    a = range(1,6)
    print(Solution().constructArr(a)) # [120, 60, 40, 30, 24]

