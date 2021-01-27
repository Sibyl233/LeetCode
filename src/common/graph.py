V = [1, 2, 3, 4, 5]
E = [[1, 2, 3, 4],
     [0, 3],
     [0, 4],
     [0, 1, 4],
     [0, 2, 3]]

visited = set()
def dfs(i):
    if i in visited:
        return
    print("visit node:", V[i])
    visited.add(i)
    for j in E[i]:
        dfs(j)

dfs(0)

from collections import deque
visited = set()
def bfs(i):
    q = deque()
    q.append(i)
    while q:
        i = q.popleft() 
        if i in visited: 
            continue
        print("visit node:", V[i])
        visited.add(i)
        for j in E[i]:  
            q.append(j)
bfs(0)

