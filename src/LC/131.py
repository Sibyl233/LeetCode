from typing import List

"""解法1_1：回溯
- 时间复杂度：O(n*2^n)
- 空间复杂度：O(n*2^n)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:    
        res,path = [],[]    

        def isPalindrome(s):
            return s == s[::-1]
        
        def backtrack(s):
            # 未探索区域满足终止条件
            if not s: 
                res.append(path[:])
                return
            # 未探索区域需要继续探索
            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):
                    path.append(s[:i])
                    backtrack(s[i:])
                    path.pop()

        backtrack(s)
        return res

"""解法1_2：回溯 + 动态规划预处理
- 时间复杂度：O(n*2^n)
- 空间复杂度：O(n*2^n)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]: 
        n = len(s)
        res,path = [],[] 

        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        
        def backtrack(i):
            if i == n:
                res.append(path[:])
                return
            for j in range(i,n):
                if dp[i][j]:
                    path.append(s[i:j+1])
                    backtrack(j+1)
                    path.pop()

        backtrack(0)
        return res

if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s)) # [['a', 'a', 'b'], ['aa', 'b']]