from typing import List

"""解法：位运算。要求①相同的数字分在同组；②两个独特的数字分在不同组。
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = a = b = 0

        # 所有数字异或，即得到 a^b
        for num in nums:
            res ^= num
        
        # 指针 p 用于找到某个不同的数位
        p = 1
        while (res & p == 0):
            p <<= 1

        # 根据 p 分成的两组必然符合2个要求
        for num in nums:
            if (num & p == 0):
                a ^= num
            else:
                b ^= num
        return [a,b]

if __name__=="__main__": 
    nums = [1,2,10,4,1,4,3,3]
    print(Solution().singleNumbers(nums)) # [2,10] 或 [10,2]