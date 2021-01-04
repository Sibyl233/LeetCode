from typing import List
import heapq

"""解法1：暴力
- 时间复杂度：O(n^2*log(n))
- 空间复杂度：O(n)
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stones.append(stones.pop()-stones.pop())
        return stones[0]

"""解法2：最大堆
- 时间复杂度：O(nlog(n))
- 空间复杂度：O(n)
"""
# 为什么用堆
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         heap = [-stone for stone in stones]
#         heapq.heapify(heap)

#         while len(heap) > 1:
#             x,y = heapq.heappop(heap),heapq.heappop(heap)
#             if x != y:
#                 heapq.heappush(heap,x-y)

#         if heap: 
#             return -heap[0]
#         return 0

if __name__ == "__main__":
    stones = [2,7,4,1,8,1]
    print(Solution().lastStoneWeight(stones)) # 1