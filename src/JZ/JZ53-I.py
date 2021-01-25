from typing import List

"""解法：二分查找
- 时间复杂度：O(logN)
- 空间复杂度：O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        def bisectRight(target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo+hi)//2
                if nums[mid] > target: 
                    hi = mid
                else: 
                    lo = mid+1
            return lo
        return bisectRight(target) - bisectRight(target-1)

if __name__=="__main__": 
    nums =  [5,7,7,8,8,10]
    target = 8
    print(Solution().search(nums, target)) # 2