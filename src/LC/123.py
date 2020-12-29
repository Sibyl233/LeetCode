# 待定
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = 2
        hold = [[0] * (k + 1) for _ in range(n)]  # hold[i][j]：恰好进行j笔交易，手上持有股票的累计最大收益
        clear = [[0] * (k + 1) for _ in range(n)] # clear[i][j]：恰好进行j笔交易，手上不持有股票的累计最大收益

        hold[0][0], clear[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            hold[0][i] = clear[0][i] = float("-inf")

        for i in range(1, n):
            hold[i][0] = max(hold[i - 1][0], clear[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                hold[i][j] = max(hold[i - 1][j], clear[i - 1][j] - prices[i])
                clear[i][j] = max(clear[i - 1][j], hold[i - 1][j - 1] + prices[i])

        return max(clear[n - 1])



if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices)) # 6