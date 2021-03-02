from typing import List

"""解法1：集合
- 时间复杂度：O(n)。采用列表会超时
- 空间复杂度：O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = set(nums) #集合
        if len(nums) <= 1:
            return None
        for num in nums:
            if target - num in nums:
                return [num, target - num]
        return None

"""解法2：双指针
- 时间复杂度：O(n)。采用列表会超时
- 空间复杂度：O(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            s = nums[left] + nums[right]
            if  s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [nums[left], nums[right]]
        return None

if __name__=="__main__": 
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target)) # [2,7]

