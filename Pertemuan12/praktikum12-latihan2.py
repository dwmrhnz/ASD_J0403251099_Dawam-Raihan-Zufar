# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# Praktikum 12 Graph II: Shortest Path
# ===========================================

# ==========================================
# Latihan 2: Implementasi Dijkstra
# ==========================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra (graph, start):
    # Fungsi untuk mencari jarak terpendek dari node start
    # ke seluruh node lain menggunakan algoritma Dijkstra.
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start adalah 0
    distances [start] = 0
    
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop (priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances [current_node]:
            continue
            
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph [current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances [neighbor]:
                distances [neighbor] = distance
                heapq.heappush (priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra (graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================
# Jawaban Analisis:
# ==========================================
# 1. Berapa jarak terpendek dari A ke B?
# Jawaban: 4
#
# 2. Berapa jarak terpendek dari A ke C?
# Jawaban: 2
#
# 3. Berapa jarak terpendek dari A ke D?
# Jawaban: 3
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jawaban: Karena algoritma mencari total akumulasi bobot terkecil. Jalur A->C->D memiliki total bobot 3 (2 + 1),
# sedangkan jalur A->B->D memiliki total bobot 9 (4 + 5).
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Jawaban: Untuk menyimpan dan selalu memprioritaskan pengecekan pada node yang memiliki jarak kumulatif terkecil saat ini. Hal ini sejalan dengan prinsip kerja Dijkstra (Greedy) yang selalu memilih jarak sementara paling kecil untuk dieksekusi lebih dulu.
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Jawaban: Karena Dijkstra menggunakan pendekatan Greedy yang berasumsi bahwa jarak terpendek ke suatu node yang sudah terpilih dari antrian tidak akan berubah lagi. Jika ada bobot negatif, jalur yang sebelumnya dianggap final bisa saja memiliki nilai yang lebih kecil lagi jika memutar lewat node lain, sehingga hasil akhirnya menjadi tidak akurat.