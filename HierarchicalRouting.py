import heapq

graph = {
    '1A': ['1B', '1C'],
    '1B': ['1A', '2A', '1C'],
    '1C': ['1A', '1B', '3B'],
    '2A': ['1B', '2B', '2C'],
    '2B': ['2A', '2D'],
    '2C': ['2A', '2D'],
    '2D': ['2B', '2C', '5C'],
    '3A': ['3B'],
    '3B': ['1C', '3A', '4A'],
    '4A': ['3B', '4B', '5A', '4C'],
    '4B': ['4A', '4C'],
    '4C': ['4A','4B'],
    '5A': ['4A', '5B', '5E'],
    '5B': ['5A', '5C'],
    '5C': ['2D', '5B', '5D'],
    '5D': ['5C', '5E'],
    '5E': ['5A', '5D'],
}

def dijkstra(graph, start, goal):
    # Priority queue untuk menyimpan node yang akan dieksplorasi
    queue = [(0, start)]
    # Dictionary untuk menyimpan jarak terpendek ke setiap node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Set untuk menyimpan node yang sudah dikunjungi
    visited = set()
    
    while queue:
        # Ambil node dengan jarak terpendek dari queue
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Jika mencapai tujuan, return jaraknya
        if current_node == goal:
            return current_distance
        
        # Update jarak ke tetangga-tetangga dari node saat ini
        for neighbor in graph[current_node]:
            distance = current_distance + 1  # Setiap edge dianggap memiliki bobot 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return float('inf')  # Return infinity jika tidak ada jalur yang ditemukan

# Input dari pengguna
start_router = input("Masukkan router awal: ")
goal_router = input("Masukkan router tujuan: ")

# Validasi input
if start_router not in graph or goal_router not in graph:
    print("Router tidak valid. Pastikan router ada dalam graf.")
else:
    hops = dijkstra(graph, start_router, goal_router)
    if hops == float('inf'):
        print(f"Tidak ada jalur dari {start_router} ke {goal_router}.")
    else:
        print(f"Jumlah hops terdekat dari {start_router} ke {goal_router} adalah: {hops}")