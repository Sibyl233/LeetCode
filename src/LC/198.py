from typing import List

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0]*(n+2)
#         for i in range(n):
#             dp[i+2] = max(dp[i+1], dp[i]+nums[i])
#         return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dp1 = 0
        for i in range(n):
            dp2 = max(dp1,dp+nums[i])
            dp = dp1
            dp1 = dp2
        return dp2

if __name__ == "__main__":
    nums = [2,7,9,3,1]
    print(Solution().rob(nums)) # 12


