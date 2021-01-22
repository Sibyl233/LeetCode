#### 二分查找一个数

```python
def bisectSearch(a, x):
    left, right = 0, len(a)-1
    while left <= right:
        mid = (left+right)//2
        if a[mid] < x: 
            left = mid+1
        elif a[mid] > x: 
            right = mid-1
        else: 
            return mid
    return -1
```

1. 适用条件：递增序列、原序列中 **x 不可重复**，可判断原序列中 x 是否存在。
2. 细节要点：
   - 初始化赋值 `right = len(a)-1`
   - 循环条件是 `while left <= right` 
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid-1`
   - 返回 mid 或 -1
3. 理解记忆：
   - 由于初始化赋值时 `right = len(a)-1` 指向最后一个元素，所以希望搜索区间 **两端都闭**  [left, right] 。
   - 循环条件为 `left <= right ` 意味着当 `left > right` 时才会终止，保证了搜索区间两端都闭。
   - 当发现 a[mid] 不是要找的 x 时，下一步要搜索的区间应该为 [left, mid-1] 或 [mid+1, right] ，正确对应搜索区间的缩小方式。
   - 当 x 存在时最后会有 `left == right` 此时返回 mid 即为目标 x 的索引；当 x 不存在时终止条件有 `left > right` 返回 -1。



#### 二分查找左（右）侧插入点

```python
def bisectLeft(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] < x: left = mid+1
        else: right = mid
    return left

def bisectRight(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] > x: right = mid
        else: left = mid+1
    return left
```

1. 适用条件：递增序列，原序列中 **x 可重复**、原序列中 **x 可以不存在**。
2. 细节要点：
   - 初始化赋值 `right = len(a)`
   - 循环条件是 `while left < right` 
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid`
   - 返回 left
3. 理解记忆：
   - 由于初始化赋值时 `right = len(a)` 越界，所以希望搜索区间 **左闭右开**  [left, right) 。
   - 循环条件为 `left < right ` 意味着当 `left == right` 时就会终止，保证了搜索区间左闭右开。
   - 当 a[mid] 被检测过后，下一步要搜索的区间应该为 [left, mid) 或 [mid+1, right) ，正确对应搜索区间的缩小方式。
   - 这里分为两个问题：① 为什么查找左（右）侧插入点都返回 left ？因为终止条件为 `left == right `，所以返回哪个都一样。② 为什么返回的 left 是左（右）侧插入点？……

#### 二分查找左（右）边界

