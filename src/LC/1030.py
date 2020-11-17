from typing import List

"""
解法1：直接排序
- 时间复杂度：O(RClog(RC))
- 空间复杂度：O(log(RC))
"""
# class Solution:
#     def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
#         res = [(i, j) for i in range(R) for j in range(C)]
#         res.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
#         return res

"""
解法2：桶排序
- 时间复杂度：O(RC)
- 空间复杂度：O(RC)
"""
# class Solution:
#     def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
#         maxDist = max(r0, R-1-r0) + max(c0, C-1-c0)
#         bucket = [[] for i in range(maxDist+1)]
#         for i in range(R):
#             for j in range(C):
#                 dist = abs(r0-i)+abs(c0-j)
#                 bucket[dist].append([i,j])
#         res = []
#         for i in range(maxDist+1):
#             res.extend(bucket[i])
#         return res

"""
解法3：BFS
- 时间复杂度：O((R+C)^2)
- 空间复杂度：O(1)
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        queue, visited = [],set()
        visited.add((r0, c0))
        queue.append((r0,c0))
        res = []
        while queue:
            p = queue.pop(0)
            res.append(list(p))
            for x in [(p[0]+1,p[1]),(p[0]-1,p[1]), (p[0],p[1]+1), (p[0],p[1]-1)]:
                if 0 <= x[0] < R and 0 <=x[1]<C and x not in visited:
                    visited.add(x)
                    queue.append(x)
        return res
        
if __name__ == "__main__":
    R, C, r0, c0 = 2, 3, 1, 2
    print(Solution().allCellsDistOrder(R,C,r0,c0)) # [(1, 2), (0, 2), (1, 1), (0, 1), (1, 0), (0, 0)]