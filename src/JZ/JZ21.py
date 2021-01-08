from typing import List

"""解法：双指针
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().exchange(nums)) # [1,3,2,4]