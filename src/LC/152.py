from typing import List

"""解法1_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         maxPro, minPro = [nums[0]], [nums[0]]
#         res = nums[0]
#         for i in range(1, len(nums)):
#             maxPro.append(max(maxPro[i-1]*nums[i], minPro[i-1]*nums[i], nums[i]))
#             minPro.append(min(maxPro[i-1]*nums[i], minPro[i-1]*nums[i], nums[i]))
#             res = max(res, maxPro[i])
#         return res

"""解法1_2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro, minPro = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            preMax, preMin = maxPro, minPro
            maxPro = max(preMax*nums[i], preMin*nums[i], nums[i])
            minPro = min(preMax*nums[i], preMin*nums[i], nums[i])
            res = max(res, maxPro)
        return res

if __name__=="__main__": 
    nums = [-2,3,-4]
    print(Solution().maxProduct(nums)) # 24

