import collections

"""解法1：字典存储频数
- 时间复杂度：O(n)
- 空间复杂度：O(26)
"""
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         frequency = collections.Counter(s)
#         for i, ch in enumerate(s):
#             if frequency[ch] == 1:
#                 return i
#         return -1

"""解法2_1：字典存储索引
- 时间复杂度：O(n)
- 空间复杂度：O(26)
"""
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         position = dict()
#         n = len(s)
#         for i, ch in enumerate(s):
#             if ch in position:
#                 position[ch] = -1
#             else:
#                 position[ch] = i
#         first = n
#         for pos in position.values():
#             if pos != -1 and pos < first:
#                 first = pos
#         if first == n:
#             first = -1
#         return first

"""解法2_2：字典存储索引+队列
- 时间复杂度：O(n)
- 空间复杂度：O(26)
"""
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         position = dict()
#         q = collections.deque()
#         for i, ch in enumerate(s):
#             if ch not in position:
#                 position[ch] = i
#                 q.append((s[i], i))
#             else:
#                 position[ch] = -1
#                 while q and position[q[0][0]] == -1:
#                     q.popleft()
#         return -1 if not q else q[0][1]

"""解法3：从字符串头和字符串尾查找对应字母的索引，如果两索引相等，则说明是单一字符
- 时间复杂度：O(n^2)
- 空间复杂度：O(1)
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in s:
            if s.find(ch) == s.rfind(ch):
                return s.find(ch)
        return -1

if __name__ == "__main__":
    s = "loveleetcode"
    print(Solution().firstUniqChar(s)) # 2