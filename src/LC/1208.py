from itertools import accumulate
import bisect

"""解法1：前缀和+二分法
- 时间复杂度：O(NlogN)
- 空间复杂度：O(N)
"""
# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         n = len(s)
#         accDiff = [0] + list(accumulate(abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)))
#         maxLength = 0

#         for i in range(1, n + 1):
#             start = bisect.bisect_left(accDiff, accDiff[i] - maxCost)
#             maxLength = max(maxLength, i - start)
        
#         return maxLength

"""解法2：双指针
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        maxLength = start = end = 0
        total = 0

        while end < n:
            total += diff[end]
            while total > maxCost:
                total -= diff[start]
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1
        
        return maxLength

if __name__ == "__main__":
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    print(Solution().equalSubstring(s,t,maxCost)) # 3