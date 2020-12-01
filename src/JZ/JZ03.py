from typing import List

"""
解法1：集合/哈希表
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def findRepeatNumber(self, nums: List[int]) -> int:
#         dic = set()
#         for num in nums:
#             if num in dic:
#                 return num
#             dic.add(num)
#         return -1

"""
解法2：原地交换
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

if __name__=="__main__": 
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums)) # 2或3
