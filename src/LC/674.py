from typing import List

"""解法：一次遍历+贪心
- 时间复杂度：O(n)。需要遍历数组一次。
- 空间复杂度：O(1)
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        count, res = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            res = max(res, count)
        return res

if __name__ == "__main__":
    nums = [1,3,5,4,7]
    print(Solution().findLengthOfLCIS(nums)) # 3