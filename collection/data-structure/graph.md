## 图

### 定义

从数学上定义，图是由一个节点集合 V 和一个边集合 E 构成的非线性数据结构，其中 E 定义了 V 中节点的连接关系。

### 概念

- 节点
  - 节点的度：入度和出度
  - 节点的权重
- 边
  - 边的方向：无向边 → 无向图；有向边 → 有向图。
  - 边的权重
- 路径与环
  - 路径：一个点到达另一个点
  - 环：一个点走回原点
- 图的类型
  - 有向图和无向图
  - 连通图和非连通图

### 表示

表示一个图的方法通常有 **邻接矩阵** 和 **邻接表** 两种：

```
5 - 4
|\  | \
| \ |   2
|  \| /
3 - 1

V = {1, 2, 3, 4, 5}
E = {(1, 2), (1, 3), (1, 4), (1, 5), (2, 4), (3, 5), (4, 5)}
```

- 邻接矩阵

```
V = [1, 2, 3, 4, 5]
E = [[0, 1, 1, 1, 1],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 0, 1],
     [1, 1, 0, 0, 1],
     [1, 0, 1, 1, 0]]
```

- 邻接表

```
V = [1, 2, 3, 4, 5]
E = [[1, 2, 3, 4],
     [0, 3],
     [0, 4],
     [0, 1, 4],
     [0, 2, 3]]
```

两种表示方式的操作性能如下表所示。可见在图稀疏的时候，邻接表大部分指标都要优于邻接矩阵（尤其是空间占用），这也是为什么实际题目中邻接表更加常见的原因。

| 性质                  | 邻接矩阵 | 邻接表  |
| --------------------- | -------- | ------- |
| 查询 i 和 j 是否连接  | O(1)     | O(E(i)) |
| 查询和 i 相连的节点数 | O(N)     | O(1)    |
| 遍历图                | O(N^2)   | O(E)    |
| 空间占用              | O(N^2)   | O(E)    |

### 操作

图的遍历分为深度优先搜索和广度优先搜索，下面的代码实现以邻接表为例。

- 深度优先搜索

```python
visited = set() # 记录访问过的节点
def dfs(i):
    if i in visited:           # 如果i访问过了就返回
        return
    print("visit node:", V[i]) # 否则标记i已访问，并输出
    visited.add(i)
    for j in E[i]: # 递归访问相邻节点
        dfs(j)

dfs(0)
```

- 广度优先搜索

```python
from collections import deque

visited = set() # 记录访问过的节点
def bfs(i):
    queue = deque() # 定义一个队列
    queue.append(i)
    while queue:
        i = queue.popleft() 
        if i in visited:           # 如果i访问过了就跳过
            continue
        print("visit node:", V[i]) # 否则标记i已访问，并输出
        visited.add(i)
        for j in E[i]: # 遍历相邻节点并放入队列
            queue.append(j)
            
bfs(0)
```

### 参考

1. https://leetcode-cn.com/leetbook/detail/high-frequency-algorithm-exercise/
2. https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/50e446/

