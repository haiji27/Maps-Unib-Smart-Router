import heapq

def hitung_dijkstra(graph, start, end):
    # Inisialisasi jarak semua node dengan nilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Jika sudah sampai di tujuan, bangun jalur mundur ke belakang
        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return path, distances[end]

        if current_distance > distances[current_node]:
            continue

        # Cek tetangga dari node yang sedang aktif
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
                
    return None, float('inf')