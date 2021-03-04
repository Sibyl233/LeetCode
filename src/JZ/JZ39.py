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
                
"""解法3：摩尔投票法(贪心)。如果一个数出现的次数超过一半，那么把它和与它不相同的数一一抵消，最后剩下来的一定是这个数。
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if cnt == 0:
                x = num
            if x == num:
                cnt += 1
            else:
                cnt -= 1
        return x

"""解法4：位运算？
- 时间复杂度：O()
- 空间复杂度：O()
"""

if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().majorityElement(nums)) # 2