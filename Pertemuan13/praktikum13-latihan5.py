# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# =======================
# Latihan 5
# =======================

import heapq # Memanggil library priority queue untuk efisiensi pemilihan bobot

# 1. Representasi weighted graph menggunakan dictionary
# Berdasarkan data Kasus 1: Jaringan Jalan Antar Kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
}

def prim_antarkota(graph, start_node):
    visited = set([start_node]) # Melacak kota yang sudah terhubung jaringan
    edges = [] # Antrean jalur yang tersedia
    
    # Masukkan semua jalur dari kota awal ke dalam heap
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))
        
    mst = [] # Hasil jalur yang masuk dalam rencana pembangunan
    total_cost = 0 # Akumulasi jarak/biaya minimum
    
    while edges:
        # Ambil jalur dengan jarak terpendek (priority queue)
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v) # Hubungkan kota baru ke jaringan
            mst.append((u, v, weight)) # Simpan jalur sebagai bagian dari MST
            total_cost += weight # Tambahkan jarak ke total
            
            # Tambahkan jalur dari kota yang baru terhubung ke dalam daftar evaluasi
            for next_city, w in graph[v].items():
                if next_city not in visited:
                    heapq.heappush(edges, (w, v, next_city))
                    
    return mst, total_cost

# 2. Menjalankan Implementasi Algoritma Prim
mst_result, total_dist = prim_antarkota(graph, 'Bogor')

# 3. Output MST
print("--- Rencana Pembangunan Jaringan Jalan Efisien ---")
for route in mst_result:
    print(f"Rute: {route[0]} ke {route[1]} | Jarak: {route[2]} km")

# 4. Output total bobot minimum
print("-" * 50)
print(f"Total Panjang Jalan Minimum = {total_dist} km")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Kasus apa yang dipilih?
#    Kasus 1: Jaringan Jalan Antar Kota (Bogor, Jakarta, Depok, Bandung).
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Prim.
#
# 3. Edge mana saja saja yang dipilih dalam MST?
#    - Bogor ke Depok (2 km)
#    - Depok ke Jakarta (3 km)
#    - Depok ke Bandung (4 km)
#
# 4. Berapa total bobot MST?
#    9 km.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Jalur Bogor-Jakarta (5) dan Jakarta-Bandung (6) tidak dipilih karena kota-kota 
#    tersebut sudah terhubung melalui rute lain yang lebih pendek (melalui Depok). 
#    Jika dipaksakan dibangun, akan terjadi pemborosan jalan (cycle) sepanjang 2 km 
#    sampai 3 km ekstra.