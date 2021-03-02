from typing import List
import heapq

"""解法1：排序
- 时间复杂度：O(nlogn)
- 空间复杂度：O(logn)
"""
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         arr.sort()
#         return arr[:k]

"""解法2：堆
- 时间复杂度：O(nlogk)
- 空间复杂度：O(k)
"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

if __name__ == "__main__":
    arr = [3,2,1]
    k = 2
    print(Solution().getLeastNumbers(arr, k)) # [1,2]或[2,1]