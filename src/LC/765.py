from typing import List

"""解法1：贪心算法+位运算
- 时间复杂度：O(N^2)
- 空间复杂度：O(1)
"""
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        res = 0
        for i in range(0, N - 1, 2):
            if row[i] != row[i + 1] ^ 1:
                for j in range(i + 1, N):
                    if row[i] == row[j] ^ 1:
                        row[i + 1], row[j] = row[j], row[i + 1]
                res += 1
        return res

"""解法2：并查集
- 时间复杂度：O(Nα(N))
- 空间复杂度：O(N)
"""
# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = list(range(n)) # 记录某个人的父母是谁
#         self.size = [1] * n          # 初始化的子树大小为1
#         self.n = n
#         self.setCount = n            # 当前连通分量数目
    
#     def find(self, x: int) -> int:
#         if x != self.parent[x]:                        # x不是自身的父母，即x不是该集合的代表
#             self.parent[x] = self.find(self.parent[x]) # 查找x的祖先直到找到代表,   
#         return self.parent[x]                          # 顺带路径压缩
    
#     def union(self, x: int, y: int) -> bool:
#         x, y = self.find(x), self.find(y)
#         if x == y:
#             return False
#         if self.size[x] < self.size[y]: # 保证小的合到大的
#             x, y = y, x
#         self.parent[y] = x
#         self.size[x] += self.size[y]
#         self.setCount -= 1
#         return True
    
#     def connected(self, x: int, y: int) -> bool:
#         x, y = self.find(x), self.find(y)
#         return x == y

# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         N = len(row)//2
#         uf = UnionFind(n)
#         for i in range(0,N*2,2):
#             uf.union(row[i]//2, row[i+1]//2)
#         res = 0
#         for i in range(N):
#             if i != uf.find(i):
#                 res += 1
#         return res

if __name__ == "__main__":
    row = [0, 2, 1, 3]
    print(Solution().minSwapsCouples(row)) # 1