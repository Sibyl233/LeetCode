import math
from functools import lru_cache

"""解法1：递归
- 时间复杂度：O()
- 空间复杂度：O()
"""
class Solution:
    @lru_cache(None)
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        res = -1
        for i in range(1, n):
            res = max(res, max(i * self.cuttingRope(n - i),i * (n - i)))
        return res

"""解法2：动态规划
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         dp = [0 for _ in range(n + 1)]
#         dp[2] = 1
#         for i in range(3, n + 1):
#             for j in range(i):
#                 dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
#         return dp[n]

"""解法3：找规律
- 时间复杂度：O(1)
- 空间复杂度：O(1)
"""
# class Solution:
#     def cuttingRope(self, n:int) -> int:
#         if n<=3: 
#             return n-1

#         a,b = n//3, n%3
#         if b==0:
#             return int(math.pow(3,a))
#         if b==1:
#             return int(math.pow(3,a-1)*4)

#         return int(math.pow(3,a)*2)

if __name__=="__main__": 
    n = 10
    print(Solution().cuttingRope(n)) # 36  
