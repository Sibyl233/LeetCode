from typing import List

"""解法1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n<2:
#             return n
        
#         up = [1] + [0]*(n-1)  
#         down = [1] + [0]*(n-1) 
#         for i in range(1,n):
#             if nums[i] > nums[i-1]:
#                 up[i] = max(up[i-1], down[i-1] + 1)
#                 down[i] = down[i-1]
#             elif nums[i] < nums[i-1]:
#                 up[i] = up[i-1]
#                 down[i] = max(up[i-1]+1, down[i-1])
#             else:
#                 up[i] = up[i-1]
#                 down[i] = down[i-1]
            
#         return max(up[n-1], down[n-1])

"""解法2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n<2:
#             return n
        
#         up = down = 1
#         for i in range(1,n):
#             if nums[i] > nums[i-1]:
#                 up = max(up, down+1)
#             elif nums[i] < nums[i-1]:
#                 down = max(up+1, down)
            
#         return max(up, down)

"""解法3：贪心
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        
        prevdiff = nums[1]-nums[0]
        res = (2 if prevdiff !=0 else 1)
        for i in range(2,n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                res += 1
                prevdiff = diff
                
        return res


if __name__ == "__main__":
    nums = [1,7,4,9,2,5]
    print(Solution().wiggleMaxLength(nums)) # 6