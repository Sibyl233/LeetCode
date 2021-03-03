class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a = b = c = 0 # 3个指针
        for i in range(1,n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]

if __name__ == "__main__":
    n = 10
    print(Solution().nthUglyNumber(n)) # 12