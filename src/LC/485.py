from typing import List

"""解法：遍历
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            res = max(res, cnt)
        return res

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums)) # 3