from typing import List

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
    print(Solution().sortArrayByParityII(A)) # 