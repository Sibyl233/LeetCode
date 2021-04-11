from typing import List
import collections

"""解法：BFS
- 时间复杂度：O(mn)
- 空间复杂度：O(mn)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        def bfs(x,y):
            area = 1
            queue = deque()
            queue.append((x,y))
            grid[x][y] = 0
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]==1:
                        queue.append((x+dx,y+dy))
                        grid[x+dx][y+dy] = 0
                        area += 1
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