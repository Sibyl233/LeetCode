"""解法1：动态规划
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = curLength = 0
        for i in range(len(s)):
            if s[i] not in dic or i - dic[s[i]] > curLength:
                curLength += 1
            else:
                curLength = i - dic[s[i]]
            dic[s[i]] = i # 更新哈希表
            res = max(res, curLength)
        return res

"""解法2：双指针
- 时间复杂度：O(N^2)
- 空间复杂度：O(1)
"""
# class Solution(object):
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         head, res = 0, 0
#         for tail in range(len(s)):
#             if s[tail] not in s[head:tail]:
#                 res = max(tail-head+1, res)
#             else:
#                 while s[tail] in s[head:tail]:
#                     head += 1
#         return res

"""解法3：双指针+哈希表
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         dic, head, res = {}, 0, 0
#         for tail in range(len(s)):
#             if s[tail] in dic:
#                 head = max(dic[s[tail]], head)
#             dic[s[tail]] = tail + 1
#             res = max(res, tail - head + 1)
#         return res

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s)) # 3