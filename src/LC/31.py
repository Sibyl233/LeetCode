from typing import List

"""
解法：两遍扫描
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.从后向前查找第一个升序对(a[i],a[i+1])
        i = len(nums) - 2
        while i > 0 and nums[i] <= nums[i+1]:
            i -= 1

        # 2.若找到，从后向前查找第一个较大数；若未找到，说明已是全降序序列，跳转至步骤3   
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]

        # 3.使用双指针反转区间[i+1,n)    
        left, right = i+1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().nextPermutation(nums)) # [1,3,2]