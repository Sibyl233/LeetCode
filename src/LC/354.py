from typing import List
import bisect

"""解法1：动态规划
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         n = len(envelopes)
#         if n < 1: return 0
#         envelopes.sort(key = lambda x: (x[0],-x[1])) # 技巧：高度按倒序排列
#         
#         dp = [1] * n
#         for i in range(n):
#             for j in range(i):
#                 if envelopes[j][1] < envelopes[i][1]:
#                     dp[i] = max(dp[i],dp[j]+1)
#         return max(dp)

"""解法2：动态规划+二分查找
- 时间复杂度：O(nlogn)
- 空间复杂度：O(n)
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0],-x[1])) # 技巧：高度按倒序排列
        return self.lengthOfLIS([x[1] for x in envelopes])

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
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print(Solution().maxEnvelopes(envelopes)) # 3