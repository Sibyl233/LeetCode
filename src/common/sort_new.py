def bubbleSort(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i]<nums[i+1]:
            nums[i],nums[i+1] = nums[i+1], nums[i]
    


    


if __name__ == "__main__":
    a = [1,6,3,4,9,2,5]
    
    # print(selectSort(a))
    print(bubbleSort(a))
    # print(insertSort(a))
    # print(shellSort(a))
    # print(mergeSort(a))
    # quickSort(a, 0, len(a)-1)
