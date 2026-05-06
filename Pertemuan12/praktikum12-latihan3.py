# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# Praktikum 12 Graph II: Shortest Path
# ===========================================

# ==========================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    # Fungsi untuk mencari jarak terpendek dari node start
    # ke seluruh node lain menggunakan algoritma Bellman Ford.
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start adalah 0
    distances [start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph [node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances [node] != float('inf') and distances [node] + weight < distances [neighbor]:
                    distances [neighbor] = distances [node] + weight
                    
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================
# Jawaban Analisis:
# ==========================================
# 1. Berapa bobot langsung dari A ke B?
# Jawaban: 5
#
# 2. Berapa total bobot jalur A->C->B?
# Jawaban: 2 (karena 4 + (-2) = 2)
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jawaban: Jalur A->C->B
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Jawaban: Karena algoritma ini melakukan relaksasi pada seluruh edge secara berulang (sebanyak jumlah node - 1 kali).
# Proses ini memastikan setiap node memperoleh jarak minimum yang benar meskipun harus melewati edge bernilai negatif
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Jawaban: Proses mengevaluasi setiap edge untuk memeriksa apakah jarak menuju suatu node (neighbor) bisa diperbarui menjadi lebih kecil jika melewati node perantara saat ini
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Jawaban: Dijkstra beroperasi dengan pendekatan lebih cepat, namun gagal pada bobot negatif, sedangkan Bellman Ford menggunakan pendekatan lebih lambat, namun mampu menangani graph dengan bobot negatif