from typing import List

"""解法1：排序
- 时间复杂度：O(nlogn)
- 空间复杂度：O(logn)
"""
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False

"""解法2：哈希表
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums)) # True