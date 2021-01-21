def bisectSearch(a, x):
    """Return the index where a[index] = x, assuming a is sorted and the value is distinct.
    """
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

def bisectLeft(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    If x already appears in the list, a.insert(x) will insert just before the leftmost x already there.
    """
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] < x: left = mid+1
        else: right = mid
    return left

def bisectRight(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    If x already appears in the list, a.insert(x) will insert just before the rightmost x already there.
    """
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] > x: right = mid
        else: left = mid+1
    return left

