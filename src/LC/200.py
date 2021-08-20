from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == '1' :
                        queue.append((nx,ny))
                        grid[nx][ny] = '0'
            return

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)
                    cnt += 1
        return cnt
        