from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxSumubArray(self, nums: List[int]) -> int:
#         dp = [nums[0]]
#         res = nums[0]
#         for i in range(1,len(nums)):
#             dp.append(max(dp[i-1]+nums[i], nums[i]))
#             res = max(dp[i],res)
#         return res

"""解法1_2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            maxSum = max(maxSum+nums[i], nums[i])
            res = max(maxSum,res)
        return res

        # 若要记录最大和子数组的起始和终止位置
        # start, end = 0, 0
        # for i in range(1,len(nums)):
        #     if maxSum > 0:
        #         maxSum += nums[i]
        #     else:
        #         maxSum = nums[i]
        #         startIdx = i
        #     if maxSum > res:
        #         res = maxSum
        #         start = startIdx
        #         end = i
        # return start, end, res 

"""解法2：分治（线段树）
- 时间复杂度：O(n)
- 空间复杂度：O(logn)
"""

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums)) # 6