"""解法1：逐位判断
- 时间复杂度：O(log2n)
- 空间复杂度：O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

"""解法2：巧用移位
- 时间复杂度：O(M)。M为二进制数字n中1的个数
- 空间复杂度：O(1)
"""
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             res += 1
#             n &= n - 1
#         return res

if __name__=="__main__": 
    n = 0b11111111111111111111111111111101
    print(Solution().hammingWeight(n)) # 31