from typing import List

# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n)) # 记录某个人的父母是谁
        self.size = [1] * n          # 初始化的子树大小为1
        self.n = n
        self.setCount = n            # 当前连通分量数目
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:                        # x不是自身的父母，即x不是该集合的代表
            self.parent[x] = self.find(self.parent[x]) # 查找x的祖先直到找到代表,   
        return self.parent[x]                          # 顺带路径压缩
    
    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]: # 保证小的合到大的
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        return x == y

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        
        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.union(u, v):
                    ans += 1
                else:
                    ufb.union(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.union(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.union(u, v):
                    ans += 1

        if ufa.setCount != 1 or ufb.setCount != 1:
            return -1
        return ans

if __name__ == "__main__":
    n = 4
    edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    print(Solution().maxNumEdgesToRemove(n, edges)) # 2 

     
