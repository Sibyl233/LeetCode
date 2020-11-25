import collections

"""
解法1：桶计数
- 时间复杂度：O(26*Length)
- 空间复杂度：O(26)
"""
class Solution:
    def sortString(self, s: str) -> str:
        # 构造桶
        num = [0] * 26
        for char in s:
            num[ord(char) - ord('a')] += 1
        
        # 构造字符串
        res = []
        while len(res) < len(s):
            for i in range(26):
                if num[i]:
                    res.append(chr(i + ord('a')))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    res.append(chr(i + ord('a')))
                    num[i] -= 1
        return "".join(res)

"""
解法2：调用内置函数。思路同解法1。
"""
# class Solution:
#     def sortString(self, s: str) -> str:
#         strCounter = collections.Counter(s)
#         res = []
#         flag = False
#         while strCounter:
#             keys = list(strCounter.keys())
#             keys.sort(reverse=flag)
#             flag = not flag
#             res.append(''.join(keys))
#             strCounter -= collections.Counter(keys)
#         return "".join(res)

if __name__ == "__main__":
    s = "aaaabbbbcccc"
    print(Solution().sortString(s)) # "abccbaabccba"   