
"""非递归实现"""
def dfs(graph: dict, start: str):
    visited = set()
    stack = []
    stack.append(start)

    while stack:
        vertice = stack.pop()
        if vertice not in visited:
            print(vertice, end=" ")
            visited.add(vertice)
            for neighbor in reversed(graph[vertice]):
                stack.append(neighbor)

"""递归实现"""
visited = set()
def dfs(graph: dict, vertice: str):
    if vertice not in visited:
        print(vertice, end = " ")
        visited.add(vertice)
    for neighbor in graph[vertice]:
        if neighbor not in visited:
            dfs(graph, neighbor)

if __name__ == "__main__":
    G = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    dfs(G, "A")

    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E - F