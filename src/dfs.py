from typing import Set

"""非递归实现"""
def dfs(graph: dict, s: str) -> Set[int]:
    visited = set()
    stack = []
    visited.add(s)
    stack.append(s)

    while stack:
        v = stack.pop()
        visited.add(v)
        # Differences from BFS:
        # 1) pop last element instead of first one
        # 2) add adjacent elements to stack without visiting them
        for adj in reversed(graph[v]):
            if adj not in visited:
                stack.append(adj)
    return visited

"""递归实现"""
visited = set()
def dfs(graph: dict, s: str) -> Set[int]:
    if s not in visited:
        print(s)
        visited.add(s)
    for adj in graph[s]:
        if adj not in visited:
            dfs(graph, adj)

if __name__ == "__main__":
    G = {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    print(dfs(G, "A"))