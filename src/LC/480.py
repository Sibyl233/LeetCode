from typing import List
import bisect

"""解法1：暴力法
- 时间复杂度：O(nklogk)
- 空间复杂度：O(k)
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        res = []
        for i in range(n-k+1):
            tmp = nums[i:i+k]
            tmp.sort()
            res.append((tmp[k//2] + tmp[(k - 1)//2]) / 2) # 计算中位数奇偶两种情况可以合并
        return res

"""解法2：双指针+二分插入
- 时间复杂度：O(nk)
- 空间复杂度：
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        tmp, res = [], []
        left = 0
        for right in range(len(nums)):
            bisect.insort_left(tmp, nums[right])
            if len(tmp) > k:
                tmp.pop(bisect.bisect_left(tmp, nums[left]))
                left += 1
            if len(tmp) == k:
                res.append((tmp[k//2] + tmp[(k - 1)//2]) / 2)
        return res

"""解法：堆
- 时间复杂度：
- 空间复杂度：
"""
                
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().medianSlidingWindow(nums, k)) # [1, -1, -1, 3, 5, 6]