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

1. 适用条件：递增序列（**无重复元素**）、 **可以判断**原序列中 x 是否存在。

2. 细节要点：
   - 初始化赋值 `right = len(a)-1`
   - 循环条件是 `while left <= right` 
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid-1`
   - 如果 x 存在，返回 mid；如果 x 不存在，返回 -1

3. 理解记忆：
   - 由于初始化赋值时 `right = len(a)-1` 指向最后一个元素，所以希望搜索区间 **两端都闭**  [left, right] 。
   - 循环条件为 `left <= right ` 意味着当 `left > right` 时才会终止，保证了搜索区间两端都闭。
   - 当发现 a[mid] 不是要找的 x 时，下一步要搜索的区间应该为 [left, mid-1] 或 [mid+1, right] ，正确对应搜索区间的缩小方式。
   - 当 x 存在时最后会有 `left == right` 此时返回 mid 即为目标 x 的索引；当 x 不存在时根据终止条件有 `left > right` 意味着没有找到目标值，返回 -1。



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

1. 适用条件：非递减序列（**元素可重复**）、原序列中 **x 可以不存在**、**无法判断**原序列中 x 是否存在。

2. 细节要点：

   - 初始化赋值 `right = len(a)`
   - 循环条件是 `while left < right` 
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid`
   - 返回 left
   
3. 理解记忆：

   - 由于初始化赋值时 `right = len(a)` 越界，所以希望搜索区间 **左闭右开**  [left, right) 。
   - 循环条件为 `left < right ` 意味着当 `left == right` 时就会终止，保证了搜索区间左闭右开。
   - 当 a[mid] 被检测过后，下一步要搜索的区间应该为 [left, mid) 或 [mid+1, right) ，正确对应搜索区间的缩小方式。
   - 这里分为两个问题：
     ① 为什么查找左（右）侧插入点都返回 left ？因为终止条件为 `left == right `，所以返回哪个都一样。
     ② 为什么返回的 left 是左（右）侧插入点？……

#### 二分查找左（右）边界

```python
def bisectLeftBound(a, x):
    """Return the index of leftmost x if x exist.
    """
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] < x: left = mid+1
        else: right = mid
    if left == len(a): 
        return -1
    return left if a[left] == x else -1

def bisectRightBound(a, x):
    """Return the index of rightmost x if x exist.
    """
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] > x: right = mid
        else: left = mid+1
    return left-1 if a[left-1] == x else -1
```

1. 适用条件：非递减序列（**元素可重复**）、原序列中 **x 可以不存在**。 **可以判断**原序列中 x 是否存在

2. 细节要点：

   - 初始化赋值 `right = len(a)`
   - 循环条件是 `while left < right` 
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid`
   - 如果 x 存在，返回 left（查找左边界）或 left-1 (查找右边界)；如果 x 不存在，返回 -1

3. 理解记忆：

   - 可以看作  **二分查找左（右）侧插入点** 基础上的修改，所以前三个细节要点和前者相同。
   - 与 **二分查找左（右）侧插入点** 算法的不同之处可以分为两点：
     ① **插入点** 和 **边界** 的细微不同：对于左侧来说，左边界的索引和左侧插入点是一致的，所以返回的还是 left；对于右侧来说，右边界的索引应该是右侧插入点的索引 - 1，所以返回的是 left-1。比如在 [1,2,3,3] 中，对于目标值 3 而言，右侧插入点的索引是 4，但右边界的索引是 3。
     ② 因为需要判断原序列中 x 是否存在，所以要增加 **判断条件** ：如果 x 存在，那么边界索引对应的元素必然等于 x，返回边界索引 left 或 left-1；否则说明 x 不存在，返回 -1。需要注意的是，在二分查找左边界的算法中，如果目标值 x 不存在且大于原序列的最大值，那么 left 会溢出，所以需要额外处理。