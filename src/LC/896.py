from typing import List

"""解法1：两次遍历
- 时间复杂度：O(2n)
- 空间复杂度：O(n)
"""
# class Solution:
#     def isMonotonic(self, A: List[int]) -> bool:
#         return self.isIncreasing(A) or self.isDecreasing(A)
    
#     def isIncreasing(self, A: List[int]) -> bool:
#         for i in range(len(A)-1):
#             if A[i]-A[i+1] > 0:
#                 return False
#         return True
    
#     def isDecreasing(self, A: List[int]) -> bool:
#         for i in range(len(A)-1):
#             if A[i]-A[i+1] < 0:
#                 return False
#         return True

"""解法2：一次遍历
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = dec = True
        for i in range(len(A)-1):
            if A[i]-A[i+1] > 0:
                inc = False
            if A[i]-A[i+1] > 0:
                dec = False
            if not inc and not dec: # 注意如果写成 if inc or dec：return True 是错误的
                return False
        return True
    
if __name__ == "__main__":
    A = [1,2,2,3]
    print(Solution().isMonotonic(A)) # True