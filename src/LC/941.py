from typing import List

"""解法：双指针
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l,r=0,len(A)-1
        while l<r and A[l]<A[l+1]: l+=1
        while r>l and A[r]<A[r-1]: r-=1
        return l==r and l!=0 and r!=len(A)-1

if __name__ == "__main__":
    A = [0,3,2,1]
    print(Solution().validMountainArray(A)) # True