from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return map(int,str(int(''.join(list(map(str,A)))) + K))

# a = map(str,A)                # 将[1,2,3]转['1','2','3']
# n = int(''.join(list(a)))       #  将列表转字符串 再转int  结果: 123
# count = n+k                   # 相加
# map(int,str(count))          # 将 结果转字符串 再转列表(数字不可迭代 所以转字符串)

if __name__ == "__main__":
    A = [1,2,0,0]
    K = 34
    print(Solution().addToArrayForm(A,K)) # 1234???