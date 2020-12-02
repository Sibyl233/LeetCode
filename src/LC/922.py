from typing import List

"""解法：双指针
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = [],[]
        res = []
        for a in A:
            if a%2 == 0:
                even.append(a)
            else:
                odd.append(a)
        while even and odd:
            res.append(even.pop())
            res.append(odd.pop())
        return res

if __name__ == "__main__":
    A = [4,2,5,7]
    print(Solution().sortArrayByParityII(A)) # [2, 7, 4, 5]