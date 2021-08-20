class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dic = {}
        l = 0
        res = 0
        for i in range(n):
            if s[i] in dic and dic[s[i]]>=l:
                l = dic[s[i]]+1
                dic[s[i]] = i
            else:
                dic[s[i]] = i
                res = max(res,i-l+1)
        return res