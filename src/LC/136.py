from typing import List

"""解法：位运算
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums)) # 4