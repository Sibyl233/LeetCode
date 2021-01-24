from typing import List

"""解法2：并查集
- 时间复杂度：O(mα(n))。其中 m 是数组 onnections 的长度, α 为 Ackermann 函数的反函数。
- 空间复杂度：O(n)
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        dsu = DisjointSetUnion(n)
        for x, y in connections:
            dsu.unionSet(x, y)
        
        return dsu.setCount - 1

if __name__ == "__main__":
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    print(Solution().makeConnected(n, connections)) # 2

