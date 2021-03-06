#### 常见排序算法

| 排序算法 | 平均时间复杂度 | 额外空间复杂度 | 稳定性 |
| -------- | -------------- | -------------- | ------ |
| 冒泡排序 | $O(n^2)$       | $O(1)$         | 稳定   |
| 选择排序 | $O(n^2)$       | $O(1)$         | 不稳定 |
| 插入排序 | $O(n^2)$       | $O(1)$         | 稳定   |
| 希尔排序 | $O(nlog(n))$   | $O(1)$         | 不稳定 |
| 堆排序   | $O(nlog(n))$   | $O(n)$         | 不稳定 |
| 归并排序 | $O(nlog(n))$   | $O(log(n))$    | 稳定   |
| 堆排序   | $O(nlog(n))$   | $O(1)$         | 不稳定 |
| 计数排序 | $O(n+k)$       | $O(k)$         | 稳定   |
| 桶排序   | $O(n+k)$       | $O(n+k)$       | 稳定   |
| 基数排序 | $O(nk)$        | $O(n+k)$       | 稳定   |

- n 表示数据规模，k 表示桶数
- 稳定性：排序后 2 个相等键值的元素顺序和排序之前相同
- Python 中 sort() 函数的内部实现机制结合了归并排序和插入排序。

#### 冒泡排序

- 原理：重复走访数列，交换相邻两元素。小的元素会通过交换慢慢浮到数列前端。
- 优化：设立标志位 `swapped`。若在某次遍历中元素没有发生交换，则证明该序列已经有序，退出循环。但这种改进对于提升性能来说没有什么太大作用。
- 最好情况：正序
- 最坏情况：反序

#### 选择排序

- 原理：从剩余未排序元素中寻找最小元素，放到已排序序列的末尾。
- 不受输入数据影响，时间复杂度不变

#### 插入排序

- 原理：对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

#### 希尔排序

#### 归并排序







