from typing import List

"""解法1：数组遍历
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights:
#             return 0

#         n = len(heights)
#         left, right = [0] * n, [0] * n
#         left[0], right[-1] = -1, n

#         for i in range(1, n):
#             tmp = i - 1
#             while tmp >= 0 and heights[tmp] >= heights[i]:
#                 tmp = left[tmp]
#             left[i] = tmp
#         for i in range(n - 2, -1, -1):
#             tmp = i + 1
#             while tmp < n and heights[tmp] >= heights[i]:
#                 tmp = right[tmp]
#             right[i] = tmp
            
#         res = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
#         return res

"""解法2_1：单调栈
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights:
#             return 0

#         n = len(heights)
#         left, right = [0] * n, [0] * n

#         stack = []
#         for i in range(n):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             left[i] = stack[-1] if stack else -1
#             stack.append(i)
        
#         stack = []
#         for i in range(n - 1, -1, -1):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             right[i] = stack[-1] if stack else n
#             stack.append(i)
            
#         res = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
#         return res

"""解法2_2：优化的单调栈
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        res = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return res

if __name__=="__main__": 
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights)) # 10