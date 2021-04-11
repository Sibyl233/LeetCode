"""DFS
"""
visited = set()
def dfs(i):
    if i not in visited and 其它限制条件:
        print(i) # 可替换成其它操作
        visited.add(i)
    for j in graph(i):
        dfs(j)
dfs(0)

"""BFS
"""
visited = set()
queue = collections.deque()
queue.append(i)
while queue:
    if i not in visited and 其它限制条件:
        print(i)
        visited.add(i)
    for j in graph(i):
        queue.append(i)

"""滑动窗口
"""
n = len(nums)
left, right = 0,0
sums, res = 0,0
while right < n：
    sums += nums[right]    # 注意右指针相关的操作放在循环开头进行
    while 区间[left,right]不符合题意:
        sums -= nums[left] # 先进行左指针相关的操作
        left += 1          # 再滑动左指针
    res = max(res,right-left+1)
    right += 1             # 最后滑动右指针
return res

"""二分查找（无重复元素）
"""
n = len(nums)
left,right = 0,n-1
while left<=right:
    mid = (left+right)//2
    if nums[mid] < target:
        left = mid
    elif nums[mid] > target:
        right = mid
    else:
        return mid
return -1

"""二分插入左边界
"""
n = len(nums)
left,right = 0,n
while left < right:
    mid = (left+right)//2
    if nums[mid] < target:
        left = mid+1
    else:
        right = mid
return left

"""二分查找左边界（元素可重复）
"""
n = len(nums)
left,right = 0,n
while left < right:
    mid = (left+right)//2
    if nums[mid] < target:
        left = mid+1
    else:
        right = mid
return left if nums[left]==target else -1

"""回溯法
"""
res = []
path = []
def backtrack(未探索区域):
    if 未探索区域满足结束条件:
        res.add(path) # 深度拷贝
        return
    for 选择 in 未探索区域当前可能的选择:
        if 当前选择符合要求:
            path.add(当前选择)
            backtrack(新的未探索区域)
            path.pop()
backtrack(起始探索区域)




