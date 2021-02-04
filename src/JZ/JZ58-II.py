"""解法1：字符串切片
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

"""解法2_1：列表遍历拼接（不允许用切片函数的情况下）
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def reverseLeftWords(self, s: str, n: int) -> str:
#         res = []
#         for i in range(n, len(s)):
#             res.append(s[i])
#         for i in range(n):
#             res.append(s[i])
#         return ''.join(res)

"""解法2_2：列表遍历拼接+取余运算
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def reverseLeftWords(self, s: str, n: int) -> str:
#         res = []
#         for i in range(n, n + len(s)):
#             res.append(s[i % len(s)])
#         return ''.join(res)

if __name__=="__main__": 
    s = "abcdefg"
    n = 2
    print(Solution().reverseLeftWords(s,n)) # "cdefgab"
