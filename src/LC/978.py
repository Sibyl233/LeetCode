from typing import List

"""解法1：双指针
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = 1
        left = right = 0

        while right < n-1:
            if left == right:
                if arr[left] == arr[left+1]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] and arr[right] < arr[right + 1]:
                    right += 1
                else:
                    left = right
            res = max(res, right - left + 1)
        
        return res
                
"""解法2_1：动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         n = len(arr)
#         res = 1
#         dp = [[1,1] for _ in range(n)]
#
#         for i in range(1, n):
#             if arr[i - 1] > arr[i]:
#                 dp[i][0] = dp[i - 1][1] + 1
#             elif arr[i - 1] < arr[i]:
#                 dp[i][1] = dp[i - 1][0] + 1
#             res = max(res, max(dp[i][0], dp[i][1]))
#         return res

"""解法2_2：优化的动态规划
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         n = len(arr)
#         res = 1
#         dp0 = dp1 = 1
        
#         for i in range(1, n):
#             if arr[i - 1] > arr[i]:
#                 dp0 = dp1 + 1
#                 dp1 = 1
#             elif arr[i - 1] < arr[i]:
#                 dp1 = dp0 + 1
#                 dp0 = 1 
#             else:
#                 dp0 = 1
#                 dp1 = 1
#             res = max(res, max(dp0, dp1))
#         return res

if __name__ == "__main__":
    arr = [9,4,2,10,7,8,8,1,9]
    print(Solution().maxTurbulenceSize(arr)) # 5

