from typing import List
"""解法：二分查找
- 时间复杂度：O(logN)
- 空间复杂度：O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == mid: 
                lo = mid+1
            else: 
                hi = mid
        return lo

if __name__=="__main__": 
    nums =  [0,1,3]
    print(Solution().missingNumber(nums)) # 2