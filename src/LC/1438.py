from typing import List
from collections import deque
from sortedcontainers import SortedList

"""解法1：滑动窗口+平衡树
- 时间复杂度：O(nlogn)
- 空间复杂度：O(n)
"""
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         n = len(nums)
#         s = SortedList()
#         left = right = res = 0

#         while right < n:
#             s.add(nums[right])
#             while s[-1] - s[0] > limit:
#                 s.remove(nums[left])
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1
        
#         return res

"""解法2：滑动窗口+队列
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        queMax, queMin = deque(), deque()
        left = right = res = 0

        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop() # 保证队首始终是最大的
            while queMin and queMin[-1] > nums[right]:
                queMin.pop() # 保证队首始终是最小的
            
            queMax.append(nums[right])
            queMin.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res

if __name__ == "__main__":
    nums = [10,1,2,4,7,2]
    limit = 5
    print(Solution().longestSubarray(nums, limit)) # 4

