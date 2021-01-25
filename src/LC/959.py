from typing import List

"""解法：并查集
- 时间复杂度：O(n^2*α(n))
- 空间复杂度：O(n^2)
"""
class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n      # 初始化子树的大小为1
        self.pa = list(range(n)) # 记录某个人的父母是谁
        self.setCount = n        # 记录连通分量数
    
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
        self.setCount -= 1                # 每进行一次合并，连通分量数减1
        
        return True

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DisjointSetUnion(4*n*n)

        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                idx = 4*(i*n+j)

                # 单元格内合并
                if c == '/':
                    dsu.unionSet(idx, idx+3)
                    dsu.unionSet(idx+1, idx+2)
                elif c == '\\':
                    dsu.unionSet(idx, idx+1)
                    dsu.unionSet(idx+2, idx+3)
                else:
                    dsu.unionSet(idx, idx+1)
                    dsu.unionSet(idx+1, idx+2)
                    dsu.unionSet(idx+2, idx+3)

                # 单元格间合并
                if (j+1) < n:
                    dsu.unionSet(idx+1, 4*(i*n+j+1)+3)
                if (i+1) < n:
                    dsu.unionSet(idx+2, 4*((i+1)*n+j))
        
        return dsu.setCount
                
if __name__ == "__main__":
    grid = [
            "/\\",
            "\\/"
           ]
    print(Solution().regionsBySlashes(grid)) # 5


