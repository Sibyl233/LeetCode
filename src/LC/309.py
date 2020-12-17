from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
        
#         n = len(prices)
#         # dp[i][0]: 手上持有股票的最大收益
#         # dp[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
#         # dp[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
#         dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
#         for i in range(1, n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
#             dp[i][1] = dp[i - 1][0] + prices[i]
#             dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        
#         return max(dp[-1][1], dp[-1][2])

"""解法1_2：优化动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp0, dp1, dp2 = -prices[0], 0, 0
        for i in range(1, n):
            newdp0 = max(dp0, dp2 - prices[i])
            newdp1 = dp0 + prices[i]
            newdp2 = max(dp1, dp2)
            dp0, dp1, dp2 = newdp0, newdp1, newdp2
        
        return max(dp1, dp2)

if __name__ == "__main__":
    prices = [1,2,3,0,2]
    print(Solution().maxProfit(prices)) # 3