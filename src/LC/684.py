from typing import List

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

def findSet(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent

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

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vertex = [ Node(i) for i in range(len(edges)+1) ]
        for v in vertex:
            makeSet(v)

        for x, y in edges:
            if findSet(vertex[x]) != findSet(vertex[y]):
                unionSet(vertex[x], vertex[y])
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

        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))