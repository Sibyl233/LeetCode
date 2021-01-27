V = [1, 2, 3, 4, 5]
E = [[1, 2, 3, 4],
     [0, 3],
     [0, 4],
     [0, 1, 4],
     [0, 2, 3]]

visited = set() # 记录访问过的节点
def dfs(i):
    if i in visited:           # 如果i访问过了就返回
        return
    print("visit node:", V[i]) # 否则标记i已访问并输出
    visited.add(i)
    for j in E[i]: # 递归访问相邻节点
        dfs(j)

dfs(0)

from collections import deque

visited = set() # 记录访问过的节点
def bfs(i):
    queue = deque() # 定义一个队列
    queue.append(i)
    while queue:
        i = queue.popleft() 
        if i in visited:           # 如果i访问过了就跳过
            continue
        print("visit node:", V[i]) # 否则标记i已访问并输出
        visited.add(i)
        for j in E[i]: # 遍历相邻节点并放入队列
            queue.append(j)
            
bfs(0)

