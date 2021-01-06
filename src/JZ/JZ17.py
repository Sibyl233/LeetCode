from typing import List

"""解法1：不考虑大数
- 时间复杂度：O(10^n)
- 空间复杂度：O(1)
"""
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))

"""解法2：考虑大数
- 时间复杂度：O(10^n)
- 空间复杂度：O(10^n)
- 备注：为正确表示代码，以下代码的返回值为数字字符串集拼接而成的长字符串，所以运行无法通过。
"""
# class Solution:
#     def printNumbers(self, n: int) -> [int]:
#         def dfs(x):
#             if x == n:
#                 s = ''.join(num[self.start:])
#                 if s != '0': res.append(s)
#                 if n - self.start == self.nine: self.start -= 1
#                 return
#             for i in range(10):
#                 if i == 9: self.nine += 1
#                 num[x] = str(i)
#                 dfs(x + 1)
#             self.nine -= 1
        
#         num, res = ['0'] * n, []
#         self.nine = 0
#         self.start = n - 1
#         dfs(0)
#         return ','.join(res)

if __name__=="__main__": 
    n = 3
    print(Solution().printNumbers(n))