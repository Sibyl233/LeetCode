"""
解法：遍历
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == " ":
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)

if __name__=="__main__": 
    s = "We are happy."
    print(Solution().replaceSpace(s)) # "We%20are%20happy."
