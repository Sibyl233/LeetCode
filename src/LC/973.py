from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: (x[0]**2+x[1]**2))
        return points[:K]
        
if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(Solution().kClosest(points, K)) # [[3,3],[-2,4]]  
        
        