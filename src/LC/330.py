from typing import List

"""解法：贪心算法
- 时间复杂度：O(m+logn)。m是数组nums的长度，n是给定的正整数。
- 空间复杂度：O(1)
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, idx = len(nums), 0

        while x <= n:
            if idx < length and nums[idx] <= x:
                x += nums[idx]
                idx += 1
            else:
                x <<= 1
                patches += 1
        
        return patches

if __name__ == "__main__":
    nums = [1,5,10]
    n = 20
    print(Solution().minPatches(nums, n))