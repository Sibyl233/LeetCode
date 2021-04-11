def selectSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

def insertSort(nums):
    n = len(nums)
    for i in range(n-1):
        while i >= 0 and nums[i+1] < nums[i]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i -= 1
    return nums

def shellSort(nums):
    n = len(nums)
    gap = n//2
    for i in range(n-gap):
        while i >= 0 and nums[i+gap] < nums[i]:
            nums[i], nums[i+gap] = nums[i+gap], nums[i]
            i -= 1
    return nums

def __merge(left,right):
    sorted_nums = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_nums.append(left[i])
            i += 1
        else:
            sorted_nums.append(right[j])
            j += 1
    sorted_nums += left[i:]
    sorted_nums += right[j:]
    return sorted_nums

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return __merge(left, right)

import random
def __partition(nums, l, r):
    idx = random.randint(l, r)
    nums[l], nums[idx] = nums[idx], nums[l]
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] > pivot :
            r -= 1
        while l < r and nums[l] < pivot:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[l] = pivot
    return l

def quickSort(nums, l, r):
    if l >= r:
        return nums
    mid = __partition(nums, l, r)
    quickSort(nums, l, mid-1)
    quickSort(nums, mid+1, r)



    


if __name__ == "__main__":
    a = [1,6,3,4,9,2,5]
    
    # print(selectSort(a))
    # print(bubbleSort(a))
    # print(insertSort(a))
    # print(shellSort(a))
    # print(mergeSort(a))
    # quickSort(a, 0, len(a)-1)
    print(a)