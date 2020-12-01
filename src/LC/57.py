from typing import List

"""
解法：分类讨论
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,r = newInterval
        placed = False # 设置flag以避免重复添加
        ans = []
        for li, ri in intervals:
            if li > r: 
                if not placed:
                    ans.append([l, r])
                    placed = True
                ans.append([li, ri])
            elif ri < l: 
                ans.append([li, ri])
            else: 
                l = min(l, li)
                r = max(r, ri)
        
        if not placed:
            ans.append([l, r])
        return ans

if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(Solution().insert(intervals, newInterval)) # [[1, 5], [6, 9]]