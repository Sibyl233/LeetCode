"""解法：分治
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c)) # 把 s 按照 c 分割
        return len(s)

if __name__ == "__main__":
    s = "ababbc"
    k = 2
    print(Solution().longestSubstring(s, k)) # 5