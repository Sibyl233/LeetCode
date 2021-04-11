class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            board[i][j] = '-1'
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and board[nx][ny] == 'O':
                        queue.append((nx,ny))
                        board[nx][ny] = '-1'
            return
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i==m-1 or j==n-1) and board[i][j] == 'O':
                    bfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-1':
                    board[i][j] = 'O'