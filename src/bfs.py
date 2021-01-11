from typing import Set

def bfs(graph: dict, s: str) -> Set[int]:

    visited = set() # initialize set for storing already visited vertices
    queue = [] # create a first in first out queue to store all the vertices for BFS

    # mark the start vertex as visited and enqueue it
    visited.add(s)
    queue.append(s)

    while queue:
        v = queue.pop(0)
        # loop through all adjacent vertex and enqueue it if not yet visited
        for adj in graph[v]:
            if adj not in visited:
                queue.append(adj)
                visited.add(adj)
    return visited


if __name__ == "__main__":
    G = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print(bfs(G, "A"))