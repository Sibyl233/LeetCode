from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)] # 注意 Python 默认的优先队列是小根堆
        heapq.heapify(q)

        res = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        
        return res

if __name__ == "__main__":
    nums = [4,-2]
    k = 2
    print(Solution().maxSlidingWindow(nums, k)) # [4]