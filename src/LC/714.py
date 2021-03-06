from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee) # dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])       # dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）      
        return dp[-1][0]

"""解法1_2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         n = len(prices)
#         clear, hold = 0, -prices[0]
#         for i in range(1, n):
#             clear, hold = max(clear, hold+prices[i]-fee), max(hold, clear-prices[i])
#         return clear

"""解法2：贪心算法
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         profit = 0
#         buy = prices[0] + fee
#         for i in range(1,len(prices)):
#             if prices[i] + fee < buy:
#                 buy = prices[i] + fee
#             elif prices[i] > buy:
#                 profit += prices[i] - buy
#                 buy = prices[i] # 巧妙
#         return profit

if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices, fee)) # 8



