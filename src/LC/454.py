from typing import List
import collections

"""
解法：分组+哈希表
    - 时间复杂度：O(n^2)，两次二重循环
    - 空间复杂度：O(n^2)，哈希映射所需要的空间
"""
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans

if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    print(Solution().fourSumCount(A,B,C,D)) # 2