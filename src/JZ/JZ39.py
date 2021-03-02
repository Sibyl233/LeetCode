from typing import List
import collections

"""解法1：排序
- 时间复杂度：O(nlogn)
- 空间复杂度：O(logn)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

"""解法2：哈希表
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        for key,value in dic.items():
            if value > len(nums) / 2:
                return key
                
"""解法3：摩尔投票法(巧妙)
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority

"""解法4：位运算？
- 时间复杂度：O()
- 空间复杂度：O()
"""

if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().majorityElement(nums)) # 2