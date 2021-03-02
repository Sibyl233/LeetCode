from typing import List

# class Solution:
#     def dicesProbability(self, n: int) -> List[float]:
#         dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]
        
#         # 边界处理
#         for i in range(1,7):
#             dp[1][i] = 1
        
#         # n-1个骰子的状态 -> n个骰子的状态
#         for i in range(2,n+1):
#             for j in range(i,i*6+1):
#                 for k in range(1,7):
#                     if j >= k+1:
#                         dp[i][j] += dp[i-1][j-k]
                        
#         res = []
#         for i in range(n,n*6+1):
#             res.append(dp[n][i] * 1.0 /6 ** n)
#         return res

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [0 for _ in range(6*n+1)]
        
        # 边界处理
        for i in range(1,7):
            dp[i] = 1
        
        # n-1个骰子的状态 -> n个骰子的状态
        for i in range(2,n+1):
            for j in range(6*n,i-1,-1):
                dp[j] = 0 # 注意
                for k in range(1,7):
                    if j-k >= i-1: # 注意
                        dp[j] += dp[j-k]
                        
        res = []
        for i in range(n,n*6+1):
            res.append(dp[i] * 1.0 / 6 ** n)
        return res

if __name__ == "__main__":
    n = 2
    print(Solution().dicesProbability(n)) # True