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
    If x already appears in the list, x will insert just before the leftmost x already there.
    """
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] < x: left = mid+1
        else: right = mid
    return left

def bisectRight(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    If x already appears in the list, x will insert just after the rightmost x already there.
    """
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] > x: right = mid
        else: left = mid+1
    return left

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
    # if left == len(a): 
    #     return -1
    return left-1 if a[left-1] == x else -1

a = [2,2,3,3,4]
x = 3
print(bisectLeftBound(a,x))

