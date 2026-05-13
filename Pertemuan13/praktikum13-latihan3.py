# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# =======================
# Latihan 3
# =======================

import heapq # Impor modul heapq untuk mengelola antrean prioritas (min-heap)

# Representasi weighted graph menggunakan dictionary
graph = { # Inisialisasi struktur data graph
    'A': {'B': 4, 'C': 2, 'D': 5}, # Hubungan node A ke B, C, dan D
    'B': {'A': 4, 'D': 3}, # Hubungan node B ke A dan D
    'C': {'A': 2, 'D': 1}, # Hubungan node C ke A dan D
    'D': {'A': 5, 'B': 3, 'C': 1} # Hubungan node D ke A, B, dan C
} # Penutup definisi graph

def prim(graph, start): # Fungsi algoritma Prim dengan parameter graph dan titik awal
    visited = set([start]) # Set untuk mencatat node yang sudah masuk ke dalam MST
    edges = [] # List untuk menampung kandidat edge yang terhubung dengan node aktif
    
    # Ambil semua tetangga dari node awal dan masukkan ke priority queue
    for neighbor, weight in graph[start].items(): # Iterasi tetangga dari node awal
        heapq.heappush(edges, (weight, start, neighbor)) # Masukkan tuple (bobot, asal, tujuan) ke heap
    
    mst = [] # List untuk menyimpan jalur-jalur yang terpilih menjadi MST
    total_weight = 0 # Variabel untuk menghitung akumulasi seluruh bobot MST
    
    while edges: # Perulangan selama masih ada kandidat edge dalam heap
        weight, u, v = heapq.heappop(edges) # Ambil edge dengan bobot terkecil dari priority queue
        
        if v not in visited: # Cek apakah node tujuan belum pernah dikunjungi (mencegah cycle)
            visited.add(v) # Tandai node tujuan sebagai node yang sudah terhubung
            mst.append((u, v, weight)) # Tambahkan edge yang valid ke dalam list hasil MST
            total_weight += weight # Tambahkan bobot edge tersebut ke variabel total_weight
            
            # Cari tetangga baru dari node yang baru saja masuk ke MST
            for neighbor, w in graph[v].items(): # Iterasi tetangga dari node v
                if neighbor not in visited: # Jika tetangga belum masuk ke jaringan MST
                    heapq.heappush(edges, (w, v, neighbor)) # Masukkan kandidat edge baru ke heap
                    
    return mst, total_weight # Mengembalikan hasil list MST dan total bobotnya

# Eksekusi program
mst, total = prim(graph, 'A') # Jalankan fungsi prim dengan titik awal node 'A'

print("Minimum Spanning Tree:") # Cetak judul output
for edge in mst: # Iterasi setiap edge yang terpilih dalam MST
    print(edge) # Tampilkan detail tuple edge (asal, tujuan, bobot)

print("Total bobot =", total) # Tampilkan hasil akhir total biaya minimum

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge ('A', 'C') dengan bobot 2, karena merupakan edge terkecil yang terhubung dengan node A.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim membandingkan semua edge yang terhubung dengan node-node yang sudah masuk ke 
#    dalam set 'visited', lalu memilih satu edge dengan bobot terkecil yang menuju 
#    ke node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Prim membangun MST secara bertahap dari satu node tertentu dan "tumbuh" ke node 
#    sekitarnya, sedangkan Kruskal memilih edge dengan bobot terkecil secara global 
#    dari seluruh graph tanpa mempedulikan posisi node-nya.