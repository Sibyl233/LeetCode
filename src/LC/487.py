from typing import List
import collections

"""解法1_1：滑动窗口
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         left = right = 0
#         res = 0
#         zeros = 0
#         while right < len(nums):
#             if nums[right] == 0:
#                 zeros += 1
#             while zeros > 1:
#                 if nums[left] == 0:
#                     zeros -= 1
#                 left += 1
#             res = max(res, right-left+1)
#             right += 1
#         return res

"""解法1_2：滑动窗口（无限流情况）
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        res = 0
        zeros = 0
        queue = collections.deque()
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
                queue.append(right) # 记录前面0的位置
            while zeros > 1:
                left = queue.pop() + 1
                zeros -= 1
            res = max(res, right-left+1)
            right += 1
        return res

if __name__ == "__main__":
    nums = [1,0,1,1,0]
    print(Solution().findMaxConsecutiveOnes(nums)) # 4