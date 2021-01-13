### BFS&DFS

#### 概念

BFS和DFS都是对图或树进行遍历/搜索的算法。

BFS 全称是 [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search) ，中文名是宽/广度优先搜索。所谓宽度优先，就是每次都尝试访问同一层的节点。 如果同一层都访问完了，再访问下一层。这样做的结果是，BFS 算法找到的路径是从起点开始的 **最短** 合法路径。

DFS 全称是 [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search) ，中文名是深度优先搜索。所谓深度优先，就是每次都尝试向更深的节点走。DFS 最显著的特征在于其 **递归调用自身** 。同时与 BFS 类似，DFS 会对其访问过的点打上访问标记，在遍历图时跳过已打过标记的点，以确保 **每个点仅访问一次** 。符合以上两条规则的函数，便是广义上的 DFS。

#### 实现

BFS算法：

1. 选择一个节点并将其所有相邻节点排入队列。
2. 从队列中取出一个节点，将其标记为已访问，并将其所有相邻节点放入队列中。
3. 重复此过程，直到队列为空或达到目标为止。

```python
def bfs(graph: dict, start: str):
    visited = set() # initialize set for storing already visited vertices
    queue = [] # create a first in first out queue to store all the vertices for BFS
    queue.append(start)

    while queue:
        vertice = queue.pop(0)
        if vertice not in visited:
            print(vertice, end=" ")
            visited.add(vertice)
            for neighbor in graph[vertice]:
                queue.append(neighbor)
```

DFS算法：

1. 选择一个节点并将其所有相邻节点推入堆栈。
2. 从堆栈中弹出一个节点，将其标记为已访问，并将其所有相邻节点推入堆栈。
3. 重复此过程，直到堆栈为空或达到目标为止。

```python
"""非递归实现"""
def dfs(graph: dict, start: str):
    visited = set()
    stack = []
    stack.append(start)

    while stack:
        vertice = stack.pop()
        if vertice not in visited:
            print(vertice, end=" ")
            visited.add(vertice)
            for neighbor in reversed(graph[vertice]):
                stack.append(neighbor)

"""递归实现"""
visited = set()
def dfs(graph: dict, vertice: str):
    if vertice not in visited:
        print(vertice, end = " ")
        visited.add(vertice)
    for neighbor in graph[vertice]:
        if neighbor not in visited:
            dfs(graph, neighbor)
```

驱动：

```python
if __name__ == "__main__":
    G = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    bfs(G, "A")
    dfs(G, "A")
    
    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E - F
```

#### 复杂度

#### 应用



