class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return
        m,n = len(matrix),len(matrix[0])
        res1, res2 = set(), set()
        
        def dfs(x,y,res):
            res.add((x,y))
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny]>=matrix[x][y] and (nx,ny) not in res:
                    dfs(nx,ny,res)
        
        for i in range(m):
            dfs(i,0,res1)
            dfs(i,n-1,res2)
        for j in range(n):
            dfs(0,j,res1)
            dfs(m-1,j,res2)

        
        return res1 & res2