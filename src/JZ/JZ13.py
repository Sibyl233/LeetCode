import collections

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def bfs(i):
            queue = collections.deque()
            queue.append(i)
            while queue:
                i = queue.popleft()
                if i in visited:
                    continue
                count += 1
                visited.add(i)
                for 




if __name__=="__main__": 
    m = 2
    n = 3
    k = 1
    print(Solution().movingCount(m,n,k)) # True


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