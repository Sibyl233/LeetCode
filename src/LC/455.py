from typing import List

"""解法：双指针（贪心）
- 时间复杂度：O(nlogn)。瓶颈在排序。
- 空间复杂度：O(n)
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p, q = 0, 0
        cnt = 0
        while p<len(g) and q<len(s):
            if g[p] <= s[q]:
                p += 1
                q += 1
                cnt += 1
            else:
                q += 1
        return cnt
    
if __name__ == "__main__":
    g = [1,2,3]
    s = [1,1]
    print(Solution().findContentChildren(g,s)) # 1