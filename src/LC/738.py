"""解法1：贪心
- 时间复杂度：O(logN)
- 空间复杂度：O(logN)
"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        strN = list(str(N))
        n = len(strN)
        for i in range(1, n):
            if strN[i]<strN[i-1]:                 # 找到第1个不满足递增关系的位置i
                break
        if i<n:
            while i>0 and strN[i]<strN[i-1]:
                strN[i-1] = str(int(strN[i-1])-1) # strN[i-1]自身减1，可能会破坏原有递增关系
                i-=1                              # 比较相邻数位关系，直到找到不会破坏递增关系的位置j
        for j in range(i+1, n):
            strN[j] = '9'
        return int(''.join(strN))

"""解法2：数学形式
"""
# class Solution:
#     def monotoneIncreasingDigits(self, N: int) -> int:
#         ones = 111111111
#         res = 0
#         for _ in range(9):
#             while res + ones > N:
#                 ones //= 10
#             res += ones
#         return res

if __name__ == "__main__":
    N = 10
    print(Solution().monotoneIncreasingDigits(N)) # 9

