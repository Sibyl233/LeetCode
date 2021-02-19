from typing import List

"""解法：滑动窗口
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = right = 0
        zeros = 0
        res = 0
        while right < len(A):
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

if __name__ == "__main__":
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 3
    print(Solution().longestOnes(A,K)) # 10