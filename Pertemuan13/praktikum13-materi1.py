# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [ # Inisialisasi list untuk menyimpan data seluruh edge dalam graph
    (1, 'C', 'D'), # Mendefinisikan jalur antara C dan D dengan beban/biaya 1
    (2, 'A', 'C'), # Mendefinisikan jalur antara A dan C dengan beban/biaya 2
    (3, 'B', 'D'), # Mendefinisikan jalur antara B dan D dengan beban/biaya 3
    (4, 'A', 'B'), # Mendefinisikan jalur antara A dan B dengan beban/biaya 4
    (5, 'A', 'D')  # Mendefinisikan jalur antara A dan D dengan beban/biaya 5
] # Penutup list data edge

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort() # Fungsi sorting bawaan Python untuk mengurutkan tuple berdasarkan elemen pertama (bobot)

mst = [] # List kosong untuk menyimpan jalur-jalur yang terpilih masuk ke MST
total_weight = 0 # Variabel accumulator untuk menghitung total biaya minimum

# Set untuk melacak node yang sudah terhubung
connected = set() # Menggunakan set karena pencarian (lookup) datanya lebih cepat (O(1))

for weight, u, v in edges: # Melakukan perulangan pada setiap edge yang sudah diurutkan
    # Cek apakah setidaknya satu node dari edge tersebut belum masuk ke jaringan
    if u not in connected or v not in connected: # Logika dasar untuk mencegah pembentukan cycle sederhana
        mst.append((u, v, weight)) # Memasukkan edge yang valid ke dalam struktur MST
        total_weight += weight # Menambahkan bobot edge terpilih ke akumulasi total biaya
        connected.add(u) # Menandai node u sebagai node yang sudah terhubung
        connected.add(v) # Menandai node v sebagai node yang sudah terhubung

print("Minimum Spanning Tree:") # Menampilkan teks judul hasil
for edge in mst: # Melakukan iterasi pada list MST yang sudah terbentuk
    print(edge) # Mencetak detail setiap edge terpilih (node asal, node tujuan, bobot)

print("Total bobot =", total_weight) # Menampilkan hasil akhir penjumlahan seluruh bobot MST