# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# Praktikum 12 Graph II: Shortest Path
# ===========================================

# ===============================================
# Algoritma Dijkstra
# ===============================================

import heapq # Memuat library untuk struktur data priority queue

# Struktur graph: 'Node Asal': {'Node Tujuan': Bobot}
graph = {
    'A': {'B': 4, 'C': 2}, # Node A ke B bobot 4, ke C bobot 2
    'B': {'D': 5},         # Node B ke D bobot 5
    'C': {'D': 1},         # Node C ke D bobot 1
    'D': {}                # Node D tidak memiliki tetangga keluar
}

def dijkstra (graph, start): # Mendefinisikan fungsi Dijkstra dengan input graph dan node awal
    # Inisialisasi jarak semua node sebagai tak hingga (inf)
    distances = {node: float('inf') for node in graph} 
    
    distances [start] = 0 # Jarak node awal ke dirinya sendiri disetel 0
    
    pq = [(0, start)] # Inisialisasi priority queue dengan (jarak 0, node awal)
    
    while pq: # Selama antrian priority queue tidak kosong
        # Ambil node dengan jarak kumulatif terkecil
        current_distance, current_node = heapq.heappop(pq)
        
        # Iterasi setiap tetangga dan bobot edge dari node saat ini
        for neighbor, weight in graph [current_node].items():
            # Hitung total jarak baru menuju tetangga
            distance = current_distance + weight
            
            # Jika rute baru lebih pendek dari jarak yang tersimpan
            if distance < distances [neighbor]:
                distances [neighbor] = distance # Perbarui jarak minimum ke tetangga
                heapq.heappush (pq, (distance, neighbor)) # Masukkan ke antrian untuk diproses
                
    return distances # Mengembalikan hasil akhir jarak minimum semua node

hasil = dijkstra (graph, 'A') # Menjalankan algoritma dari titik awal 'A'
print(hasil) # Mencetak hasil jarak terpendek