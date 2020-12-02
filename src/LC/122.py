from typing import List

"""解法：贪心算法
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
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