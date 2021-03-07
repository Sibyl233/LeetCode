"""解法1：两遍扫描。同LC31。
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            return -1
   
        left, right = i+1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        res = int("".join(nums))
        return res if res < 2**31 else -1
        
"""解法2：单调栈。
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""

if __name__ == "__main__":
    n = 12
    print(Solution().nextGreaterElement(n)) # 21