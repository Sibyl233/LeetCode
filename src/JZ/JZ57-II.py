from typing import List

"""解法1：暴力枚举
- 时间复杂度：O(target*sqrt(target))
- 空间复杂度：O(1)
"""
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         res = []
#         for i in range(1,target//2+1):
#             s = 0 # 序列和
#             for j in range(i,target//2+2): # 注意取值范围
#                 s += j
#                 if s > target:
#                     break
#                 elif s == target:
#                     res.append(list(range(i, j+1)))
#                     break
#         return res

"""解法2：数学求根
- 时间复杂度：O(target)
- 空间复杂度：O(1)
"""
# class Solution:
#     def findContinuousSequence(self, target: int):
#         i, j = 1, 2
#         res = []
#         while i < j:
#             j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
#             if j == int(j):
#                 res.append(list(range(i, int(j) + 1)))
#             i += 1
#         return res

"""解法3：滑动窗口
- 时间复杂度：O(target)
- 空间复杂度：O(1)
"""
class Solution:
    def findContinuousSequence(self, target: int):
        left = right = 1
        s = 0
        res = []
        while left <= target//2:
            if s < target:
                s += right
                right += 1
            if s > target:
                s -= left
                left += 1
            elif s == target:
                res.append(list(range(left, right))) # 注意范围
                s -= left
                left += 1
        return res

if __name__=="__main__": 
    target = 9
    print(Solution().findContinuousSequence(target)) # [[2,3,4],[4,5]]
