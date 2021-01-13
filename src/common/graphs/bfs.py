def bfs(graph: dict, start: str):
    visited = set() # initialize set for storing already visited vertices
    queue = [] # create a first in first out queue to store all the vertices for BFS
    queue.append(start)

    while queue:
        vertice = queue.pop(0)
        if vertice not in visited:
            print(vertice, end=" ")
            visited.add(vertice)
            for neighbor in graph[vertice]:
                queue.append(neighbor)


if __name__ == "__main__":
    G = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    bfs(G, "A")

    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E - F
