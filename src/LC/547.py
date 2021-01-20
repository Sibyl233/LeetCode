from typing import List
import collections

"""解法1：DFS
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(cities):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        cities = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces += 1
        
        return provinces

"""解法2：BFS
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         cities = len(isConnected)
#         visited = set()
#         provinces = 0
        
#         for i in range(cities):
#             if i not in visited:
#                 Q = collections.deque([i])
#                 while Q:
#                     j = Q.popleft()
#                     visited.add(j)
#                     for k in range(cities):
#                         if isConnected[j][k] == 1 and k not in visited:
#                             Q.append(k)
#                 provinces += 1
        
#         return provinces

"""解法3：并查集
- 时间复杂度：O(n^2α(n))
- 空间复杂度：O(n)
"""
# class DisjointSetUnion:
#     def __init__(self, n):
#         self.n = n
#         self.rank = [1] * n      # 初始化子树的大小为1
#         self.pa = list(range(n)) # 记录某个人的父母是谁
    
#     def find(self, x: int) -> int:
#         if x != self.pa[x]:                    # x不是自身的父母，即x不是该集合的代表
#             self.pa[x] = self.find(self.pa[x]) # 查找x的祖先直到找到代表,
#         return self.pa[x]                      # 顺带路径压缩
    
#     def unionSet(self, x: int, y: int) -> bool:
#         xx, yy = self.find(x), self.find(y)
        
#         if xx == yy:
#             return False
        
#         if self.rank[xx] > self.rank[yy]: # 保证小的合到大的
#             xx, yy = yy, xx
        
#         self.pa[xx] = yy
#         self.rank[yy] += self.rank[xx]
        
#         return True

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         cities = len(isConnected)
#         dsu = DisjointSetUnion(cities)
        
#         # 子集合并
#         for i in range(cities):
#             for j in range(i+1, cities):
#                 if isConnected[i][j] == 1:
#                     dsu.unionSet(i,j)
        
#         # 计算集合个数
#         circles = set()
#         for i in range(cities):
#             circles.add(dsu.find(i))
#         return len(circles)

if __name__ == "__main__":
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected)) # 3