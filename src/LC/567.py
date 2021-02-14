"""解法：滑动窗口
- 时间复杂度：O(m+n+|Σ|)
- 空间复杂度：O(|Σ|)
"""
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         m, n = len(s1), len(s2)
#         if m > n:
#             return False
        
#         cnt1, cnt2 = [0]*26, [0]*26
#         for i in range(m):
#             cnt1[ord(s1[i])-ord('a')] += 1
#             cnt2[ord(s2[i])-ord('a')] += 1
#         if cnt1 == cnt2:
#             return True

#         for i in range(m,n):
#             cnt2[ord(s2[i-m])-ord('a')] -= 1
#             cnt2[ord(s2[i])-ord('a')] += 1
#             if cnt1 == cnt2:
#                 return True

#         return False

import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
            
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter(s2[0:len(s1)])
        if cnt1 == cnt2:
            return True
          
        for i in range(m,n):
            cnt2[s2[i-m]] -= 1
            if cnt2[s2[i-m]] == 0: #注意
                del cnt2[s2[i-m]]
            cnt2[s2[i]] += 1
            if cnt1 == cnt2:
                return True  
                
        return False

if __name__ == "__main__":
    s1 = "ab" 
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1,s2)) # True