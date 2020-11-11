from typing import List
from functools import lru_cache

# 解法1：动态规划
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         dp = [False]*(n+1)
#         dp[0] = True
#         for i in range(n):
#             for j in range(i+1,n+1):
#                 if dp[i] and s[i:j] in wordDict:
#                     dp[j] = True
#         return dp[-1]


# 解法2：回溯法
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def backtrack(s: str) -> bool:
            if not s:
                return True # s已拆分完
            res = False     # s未拆分完
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    res = backtrack(s[i:]) or res
            return res
        return backtrack(s)

if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict)) # True