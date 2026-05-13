# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# =======================
# Latihan 4
# =======================

# Representasi weighted graph menggunakan daftar edge (bobot, asal, tujuan)
# Data diambil dari deskripsi kasus Jaringan Kabel Antar Gedung
kabel_gedung = [
    (4, 'GedungA', 'GedungB'), # Biaya pemasangan A-B
    (2, 'GedungA', 'GedungC'), # Biaya pemasangan A-C
    (3, 'GedungB', 'GedungD'), # Biaya pemasangan B-D
    (1, 'GedungC', 'GedungD'), # Biaya pemasangan C-D
    (5, 'GedungA', 'GedungD')  # Biaya pemasangan A-D
]

# Urutkan berdasarkan biaya terkecil (Prinsip Kruskal)
kabel_gedung.sort()

mst_kabel = []
total_biaya = 0
gedung_terhubung = set()

# Proses pemilihan jalur kabel
for biaya, u, v in kabel_gedung:
    # Pilih jalur jika tidak membentuk cycle (sederhana)
    if u not in gedung_terhubung or v not in gedung_terhubung:
        mst_kabel.append((u, v, biaya))
        total_biaya += biaya
        gedung_terhubung.add(u)
        gedung_terhubung.add(v)

# Output hasil
print("--- Rencana Pemasangan Jaringan Kabel Minimum ---")
for jalur in mst_kabel:
    print(f"Jalur: {jalur[0]} - {jalur[1]} | Biaya: {jalur[2]}")

print("-" * 50)
print("Total Biaya Minimum Pemasangan =", total_biaya)

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
#
# 2. Edge mana saja yang dipilih?
#    GedungC-GedungD (1), GedungA-GedungC (2), dan GedungB-GedungD (3).
#
# 3. Berapa total biaya minimum?
#    6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya adalah menghubungkan semua gedung (node) agar saling 
#    terkoneksi dalam satu jaringan tanpa ada jalur ganda yang mubazir (cycle), 
#    sehingga anggaran biaya pembangunan kabel bisa ditekan seminimal mungkin.