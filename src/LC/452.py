from typing import List

"""解法：排序
- 时间复杂度：O(nlog(n))
- 空间复杂度：O(log(n))
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda point:point[1]) # 为什么要右端排序？
        pos = points[0][1]
        res = 1
        for point in points:
            if point[0] > pos:
                pos = point[1]
                res += 1

        return res

if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(Solution().findMinArrowShots(points)) # 2