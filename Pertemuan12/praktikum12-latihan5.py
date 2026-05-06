# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# Praktikum 12 Graph II: Shortest Path
# ===========================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Bobot merepresentasikan jarak antarkota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

# 2. Fungsi Dijkstra

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 3. Input node awal penentuan dalam program 
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node sesuai format
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")


# ==========================================
# Jawaban Analisis:
# ==========================================
# 1. Node awal yang digunakan apa?
# Jawaban: Bogor
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Jawaban: Depok, dengan jarak 2. (Jarak ke Bogor adalah 0, namun Depok adalah kota tujuan terdekat)
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Jawaban: Bandung, dengan jarak 8
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat
# Jawaban:
# - Algoritma mulai dari Bogor (jarak 0). Tetangga yang dievaluasi adalah Jakarta (jarak sementara 5) dan Depok (jarak sementara 2)
# - Depok dipilih untuk diproses lebih dulu karena memiliki bobot terkecil di antrian (2)
# - Dari Depok, algoritma mengevaluasi rute ke Jakarta (jarak 2 + 2 = 4) dan Bandung (jarak 2 + 6 = 8)
# - Karena rute Bogor -> Depok -> Jakarta (4) lebih kecil dari rute langsung Bogor -> Jakarta (5), jarak ke Jakarta di-update menjadi 4. Jarak sementara ke Bandung dicatat sebagai 8
# - Selanjutnya Jakarta diproses. Tetangganya adalah Bandung (jarak 4 + 7 = 11). Karena 11 lebih besar dari jarak ke Bandung yang sudah ditemukan sebelumnya (8), jarak tidak di-update
# - Hasil akhir jarak terpendek didapatkan: Jakarta = 4, Depok = 2, Bandung = 8
