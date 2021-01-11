from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # dp[i][0]表示第 i 天交易完成手中不持有股票的最大金额数；
#         # dp[i][1]表示第 i 天交易完成后手中持有一只股票的最大金额数。
#         n = len(prices)
#         dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
#         for i in range(1,n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) 
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]) 
#         return dp[-1][0]

"""解法1_2：优化的动态规划。发现当天的状态只与前一天有关。
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy+prices[i]), max(buy, sell-prices[i])
        return sell

"""解法2：贪心算法
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(1,len(prices)):
#             diff = prices[i]-prices[i-1]
#             if diff > 0: 
#                 profit += diff
#         return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 7