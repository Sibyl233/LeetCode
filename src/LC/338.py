from typing import List

"""解法0：本人的直接计算
- 时间复杂度：O(k*num)。其中k = 32
- 空间复杂度：O(1)
"""
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         bits = [] 
#         for i in range(num+1):
#             ones = 0
#             x = i
#             while x > 0:
#                 ones += x&1 # x&1  表示x除以2的余数
#                 x = x>>1    # x>>1 表示x除以2
#             bits.append(ones)
#         return bits

"""解法1：直接计算
- 时间复杂度：O(k*num)。其中k = 32
- 空间复杂度：O(1)
"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = []
        for i in range(num+1):
            ones = 0
            x = i
            while x > 0:
                x &= (x-1) # x&(x-1) 表示将x二进制的最后一个1变成0
                ones += 1
            bits.append(ones)
        return bits

"""解法2：动态规划-最高有效位。需要找规律。
- 时间复杂度：O(num)
- 空间复杂度：O(1)
"""
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         bits =[0] 
#         highBit = 0 # 最高有效位：比如7的最高有效位为4
#         for i in range(1,num+1):
#             if i & (i-1) == 0: # 利用 x&(x-1) 判断当前数字是否为2的整数幂
#                 highBit = i    # 更新最高有效位
#             bits.append(bits[i-highBit] + 1) # 比如bits[7]比bits[3]多1
#         return bits

"""解法3：动态规划-最低有效位
- 时间复杂度：O(num)
- 空间复杂度：O(1)
"""
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         bits =[0] 
#         for i in range(1,num+1):
#             # 如果x是偶数，则bits[x]=bits[x//2]
#             # 如果x是奇数，则bits[x]=bits[x//2]+1
#             # 两种情况可以合并：用 x>>1 表示x除以2，用 x&1 表示x除以2的余数
#             bits.append(bits[i>>1] + (i & 1))
#         return bits

"""解法4：动态规划-最低设置位。思路和解法2对应。
- 时间复杂度：O(num)
- 空间复杂度：O(1)
"""
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         bits =[0] 
#         for i in range(1,num+1):
#             bits.append(bits[i & (i-1)] + 1)
#         return bits               

if __name__ == "__main__":
    num = 5
    print(Solution().countBits(num)) # [0,1,1,2,1,2]