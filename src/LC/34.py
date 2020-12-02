from typing import List

"""解法：两次二分查找
- 时间复杂度：O(logN)
- 空间复杂度：O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return[-1,-1]
        
        # 第一次二分查找：找到元素的开始位置
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if target > nums[mid]: lo = mid+1 
            else: hi = mid
        
        if lo >= len(nums) or nums[lo] > target: # 条件1说明所有元素都小于target；条件2说明不存在该元素。
            return[-1, -1]
        else:
            # 第二次二分查找：找到元素的结束位置
            start  = lo
            hi = len(nums)
            while lo < hi:
                mid = (lo+hi)//2
                if target >= nums[mid]: lo = mid+1 # 注意这里是大于等于
                else: hi = mid
            end = lo-1
    
        return [start,end]

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(Solution().searchRange(nums, target)) # [3,4]