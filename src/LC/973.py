from typing import List

"""解法：排序
- 时间复杂度：O(nlog(n))
- 空间复杂度：O(log(n))
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: (x[0]**2+x[1]**2))
        return points[:K]
        
if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(Solution().kClosest(points, K)) # [[3,3],[-2,4]]  
        
        