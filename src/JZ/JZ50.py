"""解法1：哈希表
- 时间复杂度：O(N)。N为字符串s的长度。
- 空间复杂度：O(1)
"""
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '

"""解法2：有序哈希表
- 时间复杂度：O(N)。N为字符串s的长度。
- 空间复杂度：O(1)
"""
# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         dic = collections.OrderedDict()
#         for c in s:
#             dic[c] = not c in dic
#         for k, v in dic.items():
#             if v: return k
#         return ' '

if __name__ == "__main__":
    s = "abaccdeff"
    print(Solution().firstUniqChar(s)) # "b"