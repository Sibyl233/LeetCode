from typing import List

"""解法2：并查集
- 时间复杂度：O(nα(n))。其中 α 为 Ackermann 函数的反函数。
- 空间复杂度：O(n)
"""
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
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DisjointSetUnion(2*10001)
        
        for x, y in stones:
            dsu.unionSet(x, y + 10001)
        
        root = set()
        for x, _ in stones:
            root.add(dsu.find(x))
        
        return len(stones) - len(root)      

if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(Solution().removeStones(stones)) # 5