from typing import List
import collections

"""解法1：DFS
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         def dfs(i: int):
#             for j in range(provinces):
#                 if isConnected[i][j] == 1 and j not in visited:
#                     visited.add(j)
#                     dfs(j)
        
#         provinces = len(isConnected)
#         visited = set()
#         circles = 0

#         for i in range(provinces):
#             if i not in visited:
#                 dfs(i)
#                 circles += 1
        
#         return circles

"""解法2：BFS
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         provinces = len(isConnected)
#         visited = set()
#         circles = 0
        
#         for i in range(provinces):
#             if i not in visited:
#                 Q = collections.deque([i])
#                 while Q:
#                     j = Q.popleft()
#                     visited.add(j)
#                     for k in range(provinces):
#                         if isConnected[j][k] == 1 and k not in visited:
#                             Q.append(k)
#                 circles += 1
        
#         return circles

"""解法3：并查集
- 时间复杂度：O(n^2logn)
- 空间复杂度：O(n)
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)
        
        provinces = len(isConnected)
        parent = list(range(provinces))
        
        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        circles = sum(parent[i] == i for i in range(provinces))
        return circles

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected)) # 4