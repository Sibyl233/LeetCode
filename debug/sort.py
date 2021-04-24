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

def selectSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if nums[j]<nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

def insertSort(nums):
    n = len(nums)
    for i in range(n-1):
        while i>=0 and nums[i+1]<nums[i]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i -= 1
    return nums                

def shellSort(nums):
    n = len(nums)
    gap = n//2
    for i in range(n-gap):
        while i >= 0 and nums[i+gap] < nums[i]:
            nums[i], nums[i+gap] = nums[i+gap], nums[i]
            i -= gap
        gap // 2
    return nums


import numpy as np
if __name__ == '__main__':
    a = list(np.random.randint(20,size=20))
    print(a)
    print(bubbleSort(a))
    print(selectSort(a))
    print(insertSort(a))
    print(shellSort(a))