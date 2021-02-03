from typing import List
import bisect

"""解法：双指针+二分法
- 时间复杂度：？
- 空间复杂度：？
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr, res = [], []
        left = 0
        for right in range(len(nums)):
            bisect.insort_left(arr, nums[right])
            if len(arr) > k:
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                res.append((arr[k//2] + arr[(k - 1)//2]) / 2)
        return res
                
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().medianSlidingWindow(nums, k)) # [1, -1, -1, 3, 5, 6]