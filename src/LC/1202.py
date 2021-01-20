from typing import List
import collections

"""解法：并查集
- 时间复杂度：O((M+N)α(N)+NlogN)。其中 α 为 Ackermann 函数的反函数。
- 空间复杂度：O(N)
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DisjointSetUnion(len(s))
        for x, y in pairs:
            dsu.unionSet(x, y)
        
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[dsu.find(i)].append(ch)
        
        for vec in mp.values():
            vec.sort(reverse=True)
        
        ans = list()
        for i in range(len(s)):
            x = dsu.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()
        
        return "".join(ans)

if __name__ == "__main__":
    s = "dcab"
    pairs = [[0,3],[1,2]]
    print(Solution().smallestStringWithSwaps(s, pairs)) # "bacd"