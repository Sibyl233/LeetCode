from typing import List

"""解法：位运算(超级巧妙,而且可扩展成其它数字均出现次2k+1的情况)
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

if __name__ == '__main__':
    nums = [0,1,0,1,0,1,99]
    print(Solution().singleNumber(nums)) # 99