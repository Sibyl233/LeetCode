# 待定
from typing import List

"""解法：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy1: 只进行过一次买操作；
        # sell1: 进行了一次买操作和一次卖操作，即完成了一笔交易；
        # buy2: 在完成了一笔交易的前提下，进行了第二次买操作；
        # sell2: 完成了全部两笔交易。
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2

if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices)) # 6