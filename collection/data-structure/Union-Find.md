### 并查集

#### 定义

并查集是一种树形的数据结构，顾名思义，它用于处理一些不交集的 **合并** 及 **查询** 问题。 它支持两种操作：

- 查找（Find）：确定某个元素处于哪个子集；
- 合并（Union）：将两个子集合并成一个集合。

#### 代码实现

- 路径压缩
- 按秩合并

```python
class Node:
    def __init__(self, data):
        self.data = data

def makeSet(x):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x

def findSet(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent
  
def unionSet(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = findSet(x), findSet(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


```

#### 复杂度

- 时间复杂度：O(α(n))。其中 α 为阿克曼函数的反函数，其增长极其缓慢，也就是说其单次操作的平均运行时间可以认为是一个很小的常数。
- 空间复杂度：O(n)

#### 参考

https://oi-wiki.org/ds/dsu/

https://github.com/TheAlgorithms/Python/tree/master/data_structures/disjoint_set

