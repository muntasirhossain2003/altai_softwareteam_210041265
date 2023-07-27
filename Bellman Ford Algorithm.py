def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                distance = distances[vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances
