## 并查集

### 概念

并查集是一种树形的数据结构，顾名思义，它用于处理一些不交集的**合并**及**查询**问题。 它支持两种操作：

- 查找（Find）：确定某个元素处于哪个子集；
- 合并（Union）：将两个子集合并成一个集合。

### 代码实现

- 路径压缩：把在路径上的每个节点都直接连接到根上；
- 按秩合并：将一棵点数与深度都较小的集合树连接到一棵更大的集合树下。相比于任意合并，这样执行查找操作的用时更少。

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n)) # 记录某个人的父母是谁
        self.size = [1] * n          # 初始化的子树大小为1
        self.n = n
        self.setCount = n            # 当前连通分量数目
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:                        # x不是自身的父母，即x不是该集合的代表
            self.parent[x] = self.find(self.parent[x]) # 查找x的祖先直到找到代表,   
        return self.parent[x]                          # 顺带路径压缩
    
    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]: # 保证小的合到大的
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        return x == y
```

### 复杂度

- 时间复杂度：只要记住**同时使用路径压缩和按秩合并后，并查集的每个操作平均时间仅为O(α(n))**。 其中 α 为阿克曼函数的反函数，其增长极其缓慢，即单次操作的平均运行时间可认为是一个很小的常数。
- 空间复杂度：O(n)

| 时间复杂度          | 平均时间复杂度 | 最坏时间复杂度 |
| ------------------- | -------------- | -------------- |
| 无优化              | O(logn)        | O(n)           |
| 路径压缩            | O(α(n))        | O(logn)        |
| 按秩合并            | O(logn)        | O(logn)        |
| 路径压缩 + 按秩合并 | O(α(n))        | O(α(n))        |

### 应用

- [最小生成树](https://oi-wiki.org/graph/mst/)中的 Kruskal 算法
- [最近公共祖先](https://oi-wiki.org/graph/lca/)中的 Tarjan 算法
- DFS的替代算法



399、547、684、721、947、959、1202、1319、1579、1584

- 684、1579套用模板即可
- 547、1319 在模板中记录setCount
- 947、959 （二维转一维）
- 721（邮箱地址抽象为元素，并合并账户）、1202（字符抽象为点，索引对抽象为边）、
- 1584（最小生成树）
- 399 （带权并查集）

#### 参考

https://oi-wiki.org/ds/dsu/

