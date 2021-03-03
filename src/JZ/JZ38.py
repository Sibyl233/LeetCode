from typing import List

"""解法：回溯法。还没很懂
- 时间复杂度：O(n!n)
- 空间复杂度：O(n^2)
"""
class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []

        def backtrack(s, path):
            if not s:
                res.append(path)
            seen = set() # 去重
            for i in range(len(s)):
                if s[i] in seen: 
                    continue
                seen.add(s[i])
                backtrack(s[:i]+s[i+1:], path + s[i])

        backtrack(s, "")
        return res

if __name__ == "__main__":
    s = "abbc"
    print(Solution().permutation(s)) 
    # ['abbc', 'abcb', 'acbb', 'babc', 'bacb', 'bbac', 'bbca', 'bcab', 'bcba', 'cabb', 'cbab', 'cbba']