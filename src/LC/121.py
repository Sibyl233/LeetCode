from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         minprice = float('inf')
#         for price in prices:
#             minprice = min(minprice, price)
#             profit = max(profit, price-minprice)
#         return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return prices[0]
        
        buy = -prices[0]
        sell = 0
        for i in range(1,n):
            buy = max(buy, -prices[i])
            sell = max(sell, buy+prices[i])
        return sell

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 5