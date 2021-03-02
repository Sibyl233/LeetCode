from typing import List

"""解法：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)?
"""
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxS, minS = A[0], A[0]
        res1, res2 = A[0], A[0]
        for i in range(1,len(A)):
            preMax, preMin = maxS, minS
            maxS = max(preMax+A[i], A[i])
            minS = min(preMin+A[i], A[i])
            res1 = max(maxS,res1)
            res2 = min(minS,res2)
        return max(res1, sum(A)-res2) if sum(A)!=res2 else res1

if __name__ == "__main__":
    A = [5,-3,5]
    print(Solution().maxSubarraySumCircular(A)) # 10