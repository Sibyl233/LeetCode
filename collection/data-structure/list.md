### 数组和链表

#### 数组

「数组」是将相同类型的元素存储于**连续**内存空间的数据结构。

```python
# 遍历
for i in range(n):
        array[i] = xxx

# 索引
array[2]
array[-2]

# 切片
array[:10]
array[1:]
array[::5]
```

「可变数组」基于数组和扩容机制实现，相比普通数组更加灵活。

```python
# 初始化可变数组
array = []

# 尾部添加元素
array.append(2)
```

#### 链表 

「链表」以节点为单位，在内存空间的存储是**非连续**的。以单向链表为例，每个节点包含两个成员变量：值 `val`，后继节点引用 `next` 。

```python
# 定义
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

建立链表 `4 -> 5 -> 1` 

```python
# 实例化节点
n1 = ListNode(4) 
n2 = ListNode(5)
n3 = ListNode(1)

# 构建引用指向
n1.next = n2
n2.next = n3
```



优势：数组拥有高效的随机访问能力。只要给出下标，就可以用常量时间找到对应元素。（比如二分查找）

劣势：插入、删除元素都会导致大量元素被迫移动，影响效率。

总之适合读操作多，写操作少的场景。