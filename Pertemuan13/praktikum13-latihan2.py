# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# =======================
# Latihan 2
# =======================

# Daftar edge: (bobot, node1, node2) sesuai data di modul
edges = [ 
    (1, 'C', 'D'), # Inisialisasi jalur C-D dengan bobot 1
    (2, 'A', 'C'), # Inisialisasi jalur A-C dengan bobot 2
    (3, 'B', 'D'), # Inisialisasi jalur B-D dengan bobot 3
    (4, 'A', 'B'), # Inisialisasi jalur A-B dengan bobot 4
    (5, 'A', 'D')  # Inisialisasi jalur A-D dengan bobot 5
] 

# Mengurutkan seluruh edge berdasarkan bobot terkecil
edges.sort() # Langkah wajib Kruskal agar pemilihan dimulai dari biaya terendah

mst = [] # List untuk menampung jalur yang terpilih masuk ke jaringan MST
total_weight = 0 # Variabel untuk menghitung akumulasi total bobot minimum
connected = set() # Set untuk melacak node mana saja yang sudah terhubung

for weight, u, v in edges: # Melakukan perulangan untuk setiap edge hasil pengurutan
    # Memilih edge jika salah satu atau kedua node belum ada di jaringan (mencegah cycle)
    if u not in connected or v not in connected: # Evaluasi kelayakan edge
        mst.append((u, v, weight)) # Tambahkan edge ke list hasil MST
        total_weight += weight # Tambahkan bobot edge ke total akumulasi
        connected.add(u) # Masukkan node u ke dalam daftar node terhubung
        connected.add(v) # Masukkan node v ke dalam daftar node terhubung

# Menampilkan hasil eksekusi algoritma
print("Minimum Spanning Tree:") # Menampilkan judul output
for edge in mst: # Iterasi untuk menampilkan setiap jalur di MST
    print(edge) # Cetak detail edge (node1, node2, bobot)

print("Total bobot =", total_weight) # Tampilkan total biaya minimum yang ditemukan

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1, karena merupakan nilai terkecil setelah diurutkan.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena prinsip dasar Kruskal adalah mencari efisiensi biaya global dengan 
#    mengambil jalur termurah yang tersedia terlebih dahulu.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6 (1 + 2 + 3).
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (4) dan A-D (5) tidak dipilih karena semua node (A, B, C, D) sudah 
#    terkoneksi dalam satu jaringan sebelum edge tersebut diproses. Jika dipilih, 
#    jalur tersebut akan membentuk cycle (siklus) yang tidak efisien.