from typing import List
import heapq
import collections

"""解法1：优先队列
- 时间复杂度：O(nlogn)
- 空间复杂度：O(k)
"""
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         q = [(-nums[i], i) for i in range(k)] # 注意 Python 默认的优先队列是小根堆
#         heapq.heapify(q)

#         res = [-q[0][0]]
#         for i in range(k, n):
#             heapq.heappush(q, (-nums[i], i))
#             while q[0][1] <= i - k:
#                 heapq.heappop(q)
#             res.append(-q[0][0])
#         return res

"""解法2：双端队列。维护一个递减的单调队列，队首始终是最大值。
- 时间复杂度：O(n)
- 空间复杂度：O(k)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        
        res = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]: # 进来的比末尾大，弹出末尾
                q.pop()
            q.append(i)
            while q[0] <= i - k:                # 滑出已不在窗口中的元素
                q.popleft()
            res.append(nums[q[0]])
        return res

if __name__ == "__main__":
    nums = [4,-2]
    k = 2
    print(Solution().maxSlidingWindow(nums, k)) # [4]