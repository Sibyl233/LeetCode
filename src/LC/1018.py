from typing import List

"""解法：模拟。模运算法则，即保留前缀二进制的余数即可。
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        pre = 0
        for a in A:
            pre = ((pre << 1) + a) % 5
            res.append(pre == 0)
        return res

if __name__ == "__main__":
    A = [0,1,1,1,1,1]
    print(Solution().prefixesDivBy5(A)) # [true,false,false,false,true,false]

