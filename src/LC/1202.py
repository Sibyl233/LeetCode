import collections

"""解法：并查集
- 时间复杂度：O((M+N)α(N)+NlogN)。其中 α 为 Ackermann 函数的反函数。
- 空间复杂度：O(N)
"""
class Node:
    def __init__(self, data):
        self.data = data

def makeSet(x):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x

def unionSet(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = findSet(x), findSet(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def findSet(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [int]) -> str:
        vertex = [ Node(i) for i in range(len(s)) ]
        for v in vertex:
            makeSet(v)
        for x, y in pairs:
            unionSet(vertex[x], vertex[y])
        
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[findSet(vertex[i])].append(ch)
        
        for vec in mp.values():
            vec.sort(reverse=True)
        
        ans = []
        for i in range(len(s)):
            x = findSet(vertex[i])
            ans.append(mp[x][-1])
            mp[x].pop()
        
        return "".join(ans)

if __name__ == "__main__":
    s = "dcab"
    pairs = [[0,3],[1,2]]
    print(Solution().smallestStringWithSwaps(s, pairs)) # "bacd"