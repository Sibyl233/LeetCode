### 并查集

#### 概念

并查集是一种树形的数据结构，顾名思义，它用于处理一些不交集的 **合并** 及 **查询** 问题。 它支持两种操作：

- 查找（Find）：确定某个元素处于哪个子集；
- 合并（Union）：将两个子集合并成一个集合。

#### 代码实现

- 路径压缩
- 按秩合并

```python
class DisjointSetUnion:
    def __init__(self, n: int):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
```

#### 复杂度

- 时间复杂度：O(α(n))。其中 α 为阿克曼函数的反函数，其增长极其缓慢，即单次操作的平均运行时间可认为是一个很小的常数。
- 空间复杂度：O(n)

#### 应用

- [最小生成树](https://oi-wiki.org/graph/mst/)中的 Kruskal 算法
- [最近公共祖先](https://oi-wiki.org/graph/lca/)中的 Tarjan 算法

####  例题

399、547、684、721、947、1202、1584

#### 参考

https://oi-wiki.org/ds/dsu/

