from typing import List
import collections

"""解法：哈希表
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = dict(), dict()
        counter = collections.Counter()
        for idx, num in enumerate(nums):
            if num not in left:
                left[num] = idx # 保存每个元素在数组中第一次出现的位置
            right[num] = idx    # 保存每个元素在数组中最后一次出现的位置
            counter[num] += 1
        
        degree = max(counter.values())
        res = len(nums)
        for k, v in counter.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res

if __name__ == "__main__":
    nums = [1,2,2,3,1,4,2]
    print(Solution().findShortestSubArray(nums)) # 6