from collections import deque

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

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])  
    if start == goal:
        return 0
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    return len(new_path) - 1
            
            visited.add(node)
    
    return float('inf') 

start_router = input("Masukkan router awal: ")
goal_router = input("Masukkan router tujuan: ")

if start_router not in graph or goal_router not in graph:
    print("Router tidak valid. Pastikan router ada dalam graf.")
else:
    hops = bfs_shortest_path(graph, start_router, goal_router)
    if hops == float('inf'):
        print(f"Tidak ada jalur dari {start_router} ke {goal_router}.")
    else:
        print(f"Jumlah hops terdekat dari {start_router} ke {goal_router} adalah: {hops}")
