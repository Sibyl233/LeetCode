from typing import List

"""解法：排序
- 时间复杂度：O(nlogn)
- 空间复杂度：O(logn)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

if __name__ == "__main__":
    nums = [6,2,6,5,1,2]
    print(Solution().arrayPairSum(nums)) # 9

