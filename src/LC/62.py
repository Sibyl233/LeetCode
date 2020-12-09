import math

"""解法1：组合数学
- 时间复杂度：O(m)
- 空间复杂度：O(1)
"""
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return math.comb(m + n - 2, n - 1)

"""解法2_1：动态规划
- 时间复杂度：O(mn)
- 空间复杂度：O(mn)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)] # 边界条件
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

"""解法2_2：动态规划+优化
- 时间复杂度：O(mn)
- 空间复杂度：O(2n)
"""
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         pre = [1] * n
#         cur = [1] * n
#         for _ in range(1, m):
#             for j in range(1, n):
#                 cur[j] = pre[j] + cur[j-1] # 只保留最后两行
#             pre = cur[:]                   # 更新
#         return pre[-1]

"""解法2_3：动态规划+优化
- 时间复杂度：O(mn)
- 空间复杂度：O(n)
"""
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         cur = [1] * n
#         for _ in range(1, m):
#             for j in range(1, n):
#                 cur[j] += cur[j-1] # 等价于解法2_2，少用一个数组
#         return cur[-1]

if __name__ == "__main__":
    m = 7
    n = 3
    print(Solution().uniquePaths(m, n)) # 28