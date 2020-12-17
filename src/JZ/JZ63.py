from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         dp = [0] * n
#         minprice = prices[0]
#         for i in range(1,n):
#             minprice = min(minprice, prices[i])
#             dp[i] = max(dp[i-1], prices[i]-minprice)
#         return dp[-1]

"""解法1_2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for price in prices:
            minprice = min(minprice, price)
            profit = max(profit, price-minprice)
        return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 5