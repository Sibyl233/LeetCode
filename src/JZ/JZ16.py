class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

if __name__=="__main__": 
    x = 2.00000
    n = -2
    print(Solution().myPow(x, n)) # 0.25000