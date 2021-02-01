from typing import List

"""解法：哈希表
- 时间复杂度：O(m+n)。m，n 分别为序列A，B长度。
- 空间复杂度：O(m)。建立一个和序列A等大的哈希表。
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        delta = (sumA - sumB) // 2
        hashmap = set(A)
        ans = None
        for y in B:
            x = y + delta
            if x in hashmap:
                ans = [x, y]
                break
        return ans

if __name__ == "__main__":
    A = [1,2,5]
    B = [2,4]
    print(Solution().fairCandySwap(A,B)) # [5,4]