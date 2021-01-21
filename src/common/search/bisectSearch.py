def bisectLeft(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    If x already appears in the list, a.insert(x) will insert just before the leftmost x already there.
    """
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

def bisectRight(a, x):
    """Return the index where to insert item x in list a, assuming a is sorted.
    If x already appears in the list, a.insert(x) will insert just before the rightmost x already there.
    """
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] > x: hi = mid
        else: lo = mid+1
    return lo