from typing import List

class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n      # 初始化子树的大小为1
        self.pa = list(range(n)) # 记录某个人的父母是谁
    
    def find(self, x: int) -> int:
        if x != self.pa[x]:                    # x不是自身的父母，即x不是该集合的代表
            self.pa[x] = self.find(self.pa[x]) # 查找x的祖先直到找到代表,
        return self.pa[x]                      # 顺带路径压缩
    
    def unionSet(self, x: int, y: int) -> bool:
        xx, yy = self.find(x), self.find(y)
        
        if xx == yy:
            return False
        
        if self.rank[xx] > self.rank[yy]: # 保证小的合到大的
            xx, yy = yy, xx
        
        self.pa[xx] = yy
        self.rank[yy] += self.rank[xx]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DisjointSetUnion(len(edges)+1)

        for x, y in edges:
            if dsu.find(x) != dsu.find(y):
                dsu.unionSet(x, y)
            else:
                return [x, y]
        
        return []

if __name__ == "__main__":
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(Solution().findRedundantConnection(edges)) # [1,4]

    # 给定的无向图为:
    # 5 - 1 - 2
    #     |   |
    #     4 - 3
