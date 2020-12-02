from typing import List

"""解法1：元组排序
- 时间复杂度：O(mlog(m)+n)。m,n分别是两个数组长度。
- 空间复杂度：O(log(m)+n)
"""
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         def mycmp(x:int) -> (int, int):
#             return (0,rank[x]) if x in rank else (1,x)
        
#         rank = {x: i for i, x in enumerate(arr2)}
#         arr1.sort(key=mycmp) 
#         return arr1

"""解法2：计数排序
- 时间复杂度：O(m+n+upper)。upper是数组arr1中的最大值。
- 空间复杂度：O(upper)
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        freq = [0] * (upper+1)
        res = []
        for i in arr1:
            freq[i] += 1
        for i in arr2:
            res += [i] * freq[i]
            freq[i] = 0
        for i in range(upper+1):
            if freq[i] > 0:
                res += [i] * freq[i]
        return res

if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(Solution().relativeSortArray(arr1, arr2)) # [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]