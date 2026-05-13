# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ==========================================================
# Implementasi Prim
# ==========================================================

import heapq # Impor library heapq untuk manajemen priority queue (min-heap)

# Representasi weighted graph dalam bentuk dictionary
graph = { # Definisi struktur graph yang akan diproses
    'A': {'B': 4, 'C': 2, 'D': 5}, # Jalur dari A ke B(4), C(2), dan D(5)
    'B': {'A': 4, 'D': 3}, # Jalur dari B ke A(4) dan D(3)
    'C': {'A': 2, 'D': 1}, # Jalur dari C ke A(2) dan D(1)
    'D': {'A': 5, 'B': 3, 'C': 1} # Jalur dari D ke A(5), B(3), dan C(1)
} # Penutup struktur data graph

def prim(graph, start): # Fungsi untuk menjalankan algoritma Prim dari node tertentu
    visited = set([start]) # Inisialisasi set untuk mencatat node yang sudah masuk jaringan MST
    edges = [] # List untuk menampung kandidat jalur yang tersedia
    
    # Ambil tetangga pertama dari node mulai dan masukkan ke heap
    for neighbor, weight in graph[start].items(): # Iterasi semua tetangga dari node awal
        heapq.heappush(edges, (weight, start, neighbor)) # Masukkan ke heap (bobot, asal, tujuan)
    
    mst = [] # List untuk menyimpan hasil akhir jalur Minimum Spanning Tree
    total_weight = 0 # Variabel untuk menghitung akumulasi total bobot minimum
    
    while edges: # Selama masih ada jalur dalam antrean heap
        weight, u, v = heapq.heappop(edges) # Ambil jalur dengan bobot paling kecil (prioritas utama)
        
        if v not in visited: # Cek jika node tujuan belum pernah dikunjungi untuk mencegah cycle
            visited.add(v) # Tandai node tujuan sebagai node yang sudah terhubung
            mst.append((u, v, weight)) # Tambahkan jalur ini ke dalam daftar hasil MST
            total_weight += weight # Tambahkan bobot jalur terpilih ke akumulasi total
            
            # Cari jalur baru dari node yang baru saja bergabung ke jaringan
            for neighbor, w in graph[v].items(): # Cek semua tetangga dari node baru (v)
                if neighbor not in visited: # Jika tetangga tersebut belum masuk jaringan
                    heapq.heappush(edges, (w, v, neighbor)) # Masukkan jalur baru ke heap untuk evaluasi
                    
    return mst, total_weight # Kembalikan hasil akhir berupa list MST dan total bobotnya

# Menjalankan fungsi Prim
mst, total = prim(graph, 'A') # Eksekusi algoritma dimulai dari titik awal node 'A'
print("Minimum Spanning Tree:") # Cetak header hasil output
for edge in mst: # Iterasi setiap jalur hasil temuan algoritma Prim
    print(edge) # Tampilkan detail jalur (asal, tujuan, bobot)
print("Total bobot =", total) # Tampilkan total biaya/bobot minimum yang ditemukan