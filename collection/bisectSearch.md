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

1. 适用条件：递增序列、**无重复元素**。
2. 细节要点：
   - 循环条件是 `while left <= right` 
   - 初始化赋值 `right = len(a)-1`
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid-1`
   - 返回 mid 或 -1

3. 理解记忆：



#### 二分查找左侧插入点/右侧插入点

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

1. 适用条件：递增序列，**元素可重复**。

2. 细节要点：
   - 循环条件是 `while left < right` 
   - 初始化赋值 `right = len(a)`
   - 搜索区间的缩小方式为 `left = mid+1`、`right = mid`
   - 返回 left
3. 理解记忆：

