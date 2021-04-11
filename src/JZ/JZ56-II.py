from typing import List

"""解法：位计数器(超级巧妙,而且可扩展成其它数字均出现次2k+1的情况)
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            bit = 1<<i
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0: # 若题目变为其它数字均出现 2k+1 次，把这里的 3 替换成 2k+1 即可
                res |= bit
        
        return res - 2**32 if res > 2**31-1 else res # 注意检测

"""解法：哈希表
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for k,v in dic.items():
            if v == 1:
                return k

"""解法：排序+遍历
- 时间复杂度：O(nlogn)
- 空间复杂度：O(n)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        for i in range(1,len(nums)-2):
            if nums[i] != nums[i+1] and nums[i]!= nums[i-1]:
                return nums[i]

if __name__ == '__main__':
    nums = [0,1,0,1,0,1,99]
    print(Solution().singleNumber(nums)) # 99