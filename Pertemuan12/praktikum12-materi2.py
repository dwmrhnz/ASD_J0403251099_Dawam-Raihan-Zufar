# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# Praktikum 12 Graph II: Shortest Path
# ===========================================

# ===============================================
# Algoritma Bellman Ford
# =============================================== 

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Relaksasi berulang
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Eksekusi fungsi
hasil = bellman_ford(graph, 'A')
print(hasil)