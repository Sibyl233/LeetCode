"""解法1：埃氏筛
- 时间复杂度：O(nlog(log(n)))
- 空间复杂度：O(n)
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        # 埃式筛
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0 
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * len(isPrime[i * i: n: i])
        return sum(isPrime)

"""解法2：线性筛
- 时间复杂度：O(n)
- 空间复杂度：O(n)
待补充
"""

if __name__ == "__main__":
    n = 10
    print(Solution().countPrimes(n)) # 4