from typing import List

"""解法：原地修改数组
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

if __name__ == "__main__":
        nums = [4,3,2,7,8,2,3,1]
        print(Solution().findDisappearedNumbers(nums)) # [5,6]


