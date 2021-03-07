from typing import List
import collections

"""解法：BFS
- 时间复杂度：O(mn)
- 空间复杂度：O(mn)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = set()

        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            area = 0
            while q:
                (x,y) = q.popleft()
                if (x,y) not in visited and 0<=x<m and 0<=y<n and grid[x][y] == 1:
                    area += 1
                    visited.add((x,y))
                    q.append((x,y+1))
                    q.append((x,y-1))
                    q.append((x+1,y))
                    q.append((x-1,y))
            return area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res,bfs(i,j))
        return res

"""解法：DFS
- 时间复杂度：O(mn)
- 空间复杂度：O(mn)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = set()

        def dfs(x,y):
            if (x,y) not in visited and 0<=x<m and 0<=y<n and grid[x][y] == 1:
                visited.add((x,y))
                return 1 + dfs(x,y+1) + dfs(x,y-1) + dfs(x+1,y) + dfs(x-1,y)
            return 0

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res

if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(Solution().maxAreaOfIsland(grid)) # 6