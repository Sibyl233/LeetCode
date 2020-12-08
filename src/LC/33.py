from typing import List

"""解法1：两次二分查找。先找分界（LC153），再找target。
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        if target >= nums[0] and nums[-1] < nums[0]:
            lo, hi = 0, lo
        else:
            lo, hi = lo, len(nums)-1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo if nums[lo] == target else -1

if __name__=="__main__": 
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target)) # 4       