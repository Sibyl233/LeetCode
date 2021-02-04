"""解法：
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回

if __name__=="__main__": 
    s = "  hello world!  "
    print(Solution().reverseWords(s)) # "world! hello"
