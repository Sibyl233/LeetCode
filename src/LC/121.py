from typing import List

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