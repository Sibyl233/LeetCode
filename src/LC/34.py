from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return[-1,-1]
        
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if target > nums[mid]: lo = mid+1
            else: hi = mid
        
        if lo >= len(nums) or nums[lo] > target:
            return[-1, -1]
        else:
            start = end = lo
            while end < len(nums) and nums[end] == target:
                end += 1
        return [start,end-1]

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(Solution().searchRange(nums, target)) # [3,4]