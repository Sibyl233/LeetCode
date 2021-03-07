## 堆

### 定义和表示

「堆」是一种基于**完全二叉树**的数据结构，可使用数组实现。以堆为原理的排序算法称为「堆排序」，基于堆实现的数据结构为「优先队列」。堆分为大顶堆和小顶堆，大（小）顶堆中任意节点的值不大于（小于）其父节点的值。

```python
# 使用库 heapq
from heapq import heappush, heappop

# 初始化小顶堆
heap = []

# 元素入堆
heappush(heap, 1)
heappush(heap, 4)
heappush(heap, 2)
heappush(heap, 6)
heappush(heap, 8)

# 元素出堆（从小到大）
heappop(heap) # -> 1
heappop(heap) # -> 2
heappop(heap) # -> 4
heappop(heap) # -> 6
heappop(heap) # -> 8
```

### 应用

