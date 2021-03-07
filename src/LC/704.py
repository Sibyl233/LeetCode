from typing import List

"""解法：二分查找
- 时间复杂度：O(logn)
- 空间复杂度：O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums,target)) # 4