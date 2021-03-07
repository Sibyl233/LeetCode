from typing import List

"""解法1：两次二分查找。先找分界（LC154），再找target。
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi = hi - 1
        
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

        return nums[lo] == target

"""解法2：递归。
- 时间复杂度：
- 空间复杂度：
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def dfs(l,r):
            if l>r: return -1
            if r-l+1 <= 2: 
                if nums[l] == target: return l 
                if nums[r] == target: return r 
                return -1

            m = (l+r)//2
            if nums[m] == target: return m

            if nums[m] > nums[l]:
                if nums[l] <= target < nums[m]:
                    return dfs(l,m-1)
                else:
                    return dfs(m+1,r)
            
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    return dfs(m+1,r)
                else:
                    return dfs(l,m-1)
            
            else:
                lres = dfs(l,m-1)
                rres = dfs(m+1,r)
                if lres != -1:
                    return lres
                return rres
            
        return dfs(0,len(nums)-1) != -1

if __name__=="__main__": 
    nums = [2,5,6,7,0,0,1,2]
    target = 0
    print(Solution().search(nums, target)) # true 