from typing import List

"""解法：动态规划
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        lengths = [1] * n
        counts = [1] * n

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j]+1 > lengths[i]:
                        lengths[i] = lengths[j]+1
                        counts[i] = counts[j]
                    elif lengths[j]+1 == lengths[i]:
                        counts[i] += counts[j]

        tmp = max(lengths)
        return sum([counts[i] for i in range(n) if lengths[i] == tmp])        

if __name__ == "__main__":
    nums = [1,3,5,4,7]
    print(Solution().findNumberOfLIS(nums)) # 2
