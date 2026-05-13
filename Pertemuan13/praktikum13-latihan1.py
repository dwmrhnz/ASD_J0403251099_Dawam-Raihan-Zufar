# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# =======================
# Latihan 1
# =======================

# 1. Daftar edge graph sesuai ilustrasi Latihan 1
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Contoh spanning tree yang valid (menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# 3. Menampilkan daftar edge graph awal
print("Edge pada graph:")
for edge in edges:
    print(edge)

# 4. Menampilkan contoh spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 5. Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal adalah struktur asli yang memiliki semua kemungkinan jalur dan sering kali 
#    mengandung cycle. Sedangkan Spanning Tree adalah subgraph (bagian dari graph awal) 
#    yang menghubungkan seluruh node tanpa membentuk cycle sama sekali.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena cycle menyebabkan penggunaan edge yang berlebih (mubazir). Tujuan utama 
#    spanning tree adalah efisiensi; jika semua node sudah terhubung, adanya jalur 
#    melingkar hanya akan meningkatkan biaya tanpa memberikan fungsi koneksi tambahan.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree menggunakan jumlah edge minimal untuk menghubungkan n node. 
#    Rumus bakunya adalah jumlah edge = n - 1. Jumlah ini adalah batas paling efisien 
#    agar semua node saling terhubung tanpa ada jalur ganda atau siklus.