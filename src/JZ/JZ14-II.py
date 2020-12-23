"""解法：找规律
- 时间复杂度：O(logN)。为二分求余法复杂度。
- 空间复杂度：O(1)
"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: 
            return n - 1

        # 不同于JZ14-I，根据题意此处求余采用二分求余法
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2

        if b == 0: 
            return (rem * 3) % p # = 3^(a+1) % p
        if b == 1: 
            return (rem * 4) % p # = 3^a * 4 % p
        return (rem * 6) % p     # = 3^(a+1) * 2  % p

if __name__=="__main__": 
    n = 10
    print(Solution().cuttingRope(n)) # 36  
