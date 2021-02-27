from typing import List
import bisect

"""解法1：动态规划
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 1: return 0
#         dp = [1] * n

#         for i in range(1,n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i],dp[j]+1)
#         return max(dp)

"""解法2：动态规划+二分查找
- 时间复杂度：O(nlogn)
- 空间复杂度：O(n)
"""
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = []
        for i in range(len(nums)):
            idx = bisect.bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
        return len(dp)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums)) # 4