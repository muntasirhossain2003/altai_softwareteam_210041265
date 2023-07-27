def valid_path(vertices, edges):


    graph = {i: [] for i in range(vertices)}
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    visited = [False] * vertices

    def dfs(node, visited):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited)

    dfs(0, visited)

    return all(visited)

vertices = 7
edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]

result = valid_path(vertices, edges)
print(result)