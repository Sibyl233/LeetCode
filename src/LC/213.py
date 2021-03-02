from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        return max(self.robNaive(nums[1:]),self.robNaive(nums[:-1]))
    
    def robNaive(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dp1 = 0
        for i in range(n):
            dp2 = max(dp1,dp+nums[i])
            dp = dp1
            dp1 = dp2
        return dp2

if __name__ == "__main__":
    nums = [2,3,2]
    print(Solution().rob(nums)) # 3