def floyd_warshall(graph):
    distances = graph.copy()

    for k in graph:
        for i in graph:
            for j in graph:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances
