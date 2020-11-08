from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,r = newInterval
        placed = False
        ans = list()
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