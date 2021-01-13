"""Topological Sort."""
#     a
#    / \
#   b  c
#  / \
# d  e
edges = {"a": ["c", "b"], "b": ["d", "e"], "c": [], "d": [], "e": []}
vertices = ["a", "b", "c", "d", "e"]

def topological_sort(start, visited, sort):
    """Perform topolical sort on a directed acyclic graph."""
    cur = start
    visited.append(cur)
    neighbors = edges[cur]
    
    for neighbor in neighbors:
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    sort.append(cur) # if all neighbors visited add current to sort

    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    return sort


if __name__ == "__main__":
    sort = topological_sort("a", [], [])
    print(sort)