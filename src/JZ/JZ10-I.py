# from functools import lru_cache

# 解法1：递归
# class Solution:
#     @lru_cache(None) # 使用lru_cache()装饰器才可通过
#     def fib(self, n: int) -> int:
#         if n ==0: return 0
#         if n == 1: return 1
#         return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007

# 解法2：动态规划
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

if __name__=="__main__": 
    n = 5
    print(Solution().fib(n)) # 5