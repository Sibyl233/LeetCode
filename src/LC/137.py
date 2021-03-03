from typing import List

"""解法：位运算(超级巧妙)
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
            if cnt % 3 != 0:
                res |= bit
        
        return res - 2**32 if res > 2**31-1 else res

if __name__ == '__main__':
    nums = [0,1,0,1,0,1,99]
    print(Solution().singleNumber(nums)) # 99