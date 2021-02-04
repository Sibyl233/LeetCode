## 链表

###  概念

「链表」以节点为单位，在内存空间的存储是 **非连续**  的。

### 实现

以单链表为例，每个节点包含两个成员变量：值 `val`，后继节点引用 `next` 。

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


