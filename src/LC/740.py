from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=[0]*(max(nums)+1)    
        for i in nums:
            count[i]+=i
        # rob    
        n = len(count)
        dp = dp1 = 0
        for i in range(n):
            dp2 = max(dp1,dp+count[i])
            dp = dp1
            dp1 = dp2
        return dp2

if __name__ == "__main__":
    nums = [2, 2, 3, 3, 3, 4]
    print(Solution().deleteAndEarn(nums)) # 9

