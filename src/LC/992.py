from typing import List
import collections

"""解法：滑动窗口
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        def atMostK(A, K):
            left = right = 0
            cnt = collections.Counter()
            distinct = 0
            res = 0
            while right < len(A):
                if cnt[A[right]] == 0:
                    distinct += 1
                cnt[A[right]] += 1
                while distinct > K:
                    cnt[A[left]] -= 1
                    if cnt[A[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1 # 注意
                right += 1
            return res

        return atMostK(A,K) - atMostK(A,K-1)

if __name__ == "__main__":
    A = [1,2,1,2,3]
    K = 2
    print(Solution().subarraysWithKDistinct(A,K)) # 7
