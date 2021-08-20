

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


# n = int(input())
# edges = []
# nameToIdx = {}
# for _ in range(n):
#     name1,name2 = list(input().split())
#     if name1 not in nameToIdx:
#         nameToIdx[name1] = len(nameToIdx)
#     if name2 not in nameToIdx:
#         nameToIdx[name2] = len(nameToIdx)
#     edges.append([nameToIdx[name1],nameToIdx[name2]])

# uf = UnionFind(n)
# for x, y in edges:
#     if uf.find(x) != uf.find(y):
#         uf.union(x, y)
# print(uf.setCount)






    

























