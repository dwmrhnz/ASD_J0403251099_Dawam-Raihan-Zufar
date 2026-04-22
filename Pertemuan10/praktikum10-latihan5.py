# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data # simpan nilai
        self.left = None # pointer kiri (kosong)
        self.right = None # pointer kanan (kosong)

# Penjelasan alur fungsi Preorder
# Fungsi ini ngebaca pohon dari root ke bawah.
# Fungsi ini nyetak node tempat dia berdiri sekarang, menelusuri sampai habis semua anak di kiri, baru lanjut ke kanan.

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None: # pastikan node ada isinya
        print(root.data, end=" ") # cetak ke layar
        preorder(root.left) # telusuri cabang kiri
        preorder(root.right) # telusuri cabang kanan

# Penjelasan alur fungsi Tampil Struktur
# Fungsi ini cuma buat nggambar pohonnya di terminal pakai spasi tambahan, biar kelihatan mana parent dan child secara visual.

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: # jika posisi node tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # cetak dengan jarak spasi
        tampil_struktur(root.left, level + 1, "L") # cetak turunan kiri
        tampil_struktur(root.right, level + 1, "R") # cetak turunan kanan

# Penjelasan alur fungsi Rotate Left
# Ini trik buat nyeimbangin pohon yang miring ke kanan.
# Anak di kanan ditarik naik jadi root utama, terus root yang lama diturunin paksa jadi anak kirinya dia.

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right 
    # y adalah child kanan x
    # subtree kiri milik y disimpan sementara
    T2 = y.left 
    
    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2
    
    # y menjadi root baru
    return y 

if __name__ == '__main__':
    # Membuat tree yang tidak seimbang:
    # 10 -> 20 -> 30
    root = Node(10)
    root.right = Node(20)
    root.right.right = Node(30)

    print("Preorder sebelum rotasi kiri:")
    preorder(root)

    print("\n\nStruktur sebelum rotasi kiri:")
    tampil_struktur(root)

    # Melakukan rotasi kiri pada root
    root = rotate_left(root)

    print("\nPreorder sesudah rotasi kiri:")
    preorder(root)

    print("\n\nStruktur sesudah rotasi kiri:")
    tampil_struktur(root)