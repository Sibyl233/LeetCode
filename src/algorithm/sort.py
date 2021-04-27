# 冒泡排序
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swapped = True
        if not swapped:
            break
    return nums


# 选择排序
def selectSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if nums[j]<nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums


# 插入排序
def insertSort(nums):
    n = len(nums)
    for i in range(n-1):
        while i>=0 and nums[i+1]<nums[i]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i -= 1
    return nums                


# 希尔排序
def shellSort(nums):
    n = len(nums)
    gap = n//2
    for i in range(n-gap):
        while i >= 0 and nums[i+gap] < nums[i]:
            nums[i], nums[i+gap] = nums[i+gap], nums[i]
            i -= gap
        gap // 2
    return nums


# 归并排序
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    # 分
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    # 合并
    return _merge(left, right)

def _merge(left, right):
    res = [] # 辅助空间
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


# 快速排序
import random
def quickSort(nums):
    n = len(nums)
    return _qsort(nums, 0, n - 1)

def _qsort(nums, left, right):
    if left >= right:
        return nums
    # 选取 pivot，并放置于数组首位
    idx = random.randint(left, right)
    nums[idx], nums[left] = nums[left], nums[idx]
    pivot = nums[left]
    # 根据 pivot 划分数组
    i = left+1
    j = right
    while i < j:
        while i < j and nums[j] > pivot:
            j -= 1
        while i < j and nums[i] <= pivot:
            i += 1
        if i == j: break
        nums[i], nums[j] = nums[j], nums[i]
    # 固定 pivot 位置。此时 i,j 指向同一元素。
    if nums[i] > pivot:
        i -= 1
    nums[left], nums[i] = nums[i], nums[left]
    # 递归
    _qsort(nums, left, i - 1)
    _qsort(nums, i + 1, right)
    return nums


# 计数排序
def countingSort(nums):
    if not nums: 
        return []
    n = len(nums)
    _min = min(nums)
    _max = max(nums)
    buckets = [0] * (_max - _min + 1)
    for num in nums:
        buckets[num - _min] += 1
    
    ki = 0
    for i in range(n):
        while buckets[ki] == 0:
            ki += 1
        nums[i] = ki + _min
        buckets[ki] -= 1
    return nums


# 桶排序
def bucketSort(nums, bucketRange):
    if len(nums) < 2:
        return nums
    _min = min(nums)
    _max = max(nums)
    bucketNum = (_max - _min) // bucketRange + 1
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        buckets[(num - _min) // bucketRange].append(num)
        
    # 桶内排序
    res = []
    for bucket in buckets:
        if not bucket: 
            continue
        res.extend(sorted(bucket))
    return res


# 基数排序
def radixSort(nums):
    if not nums: 
        return []
    _max = max(nums)
    maxDigit = len(str(_max)) # 最大位数
    buckets = [[] for _ in range(10)]
    # 从低位开始排序
    div, mod = 1, 10
    for _ in range(maxDigit):
        for num in nums:
            buckets[num % mod // div].append(num)
        div *= 10
        mod *= 10
        i = 0
        for ki in range(10):
            for item in buckets[ki]:
                nums[i] = item
                i += 1
            buckets[ki] = []
    return nums


if __name__ == '__main__':
    import numpy as np
    a = list(np.random.randint(20,size=20))
    print(a)
    # print(bubbleSort(a))
    # print(selectSort(a))
    # print(insertSort(a))
    # print(shellSort(a))
    # print(mergeSort(a))
    # print(quickSort(a))
    print(countingSort(a))
    print(bucketSort(a,5))
    print(radixSort(a))