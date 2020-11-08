from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1,len(prices)):
            tmp = prices[i]-prices[i-1]
            if tmp>0: 
                res += tmp
        return res

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices)) # 7