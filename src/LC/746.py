from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         dp = [0] * (n + 1)
#         for i in range(2, n + 1):
#             dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
#         return dp[n]

"""解法1_2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre = cur = 0
        for i in range(2, n + 1):
            nxt = min(cur + cost[i - 1], pre + cost[i - 2])
            pre, cur = cur, nxt
        return cur

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost)) # 6
