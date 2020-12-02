from typing import List

"""解法：贪心+排序
- 时间复杂度：O(Nlog(N))
- 空间复杂度：O(log(N))
"""
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        i=0
        A.sort(reverse=True)
        while i<len(A)-2:
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
            i+=1
        return 0

if __name__ == "__main__":
    A = [3,2,3,4]
    print(Solution().largestPerimeter(A)) # 10