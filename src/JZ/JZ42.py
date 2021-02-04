from typing import List

"""解法：动态规划
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums)) # 3