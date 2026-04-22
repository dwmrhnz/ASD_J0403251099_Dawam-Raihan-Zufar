# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data # simpan nilai
        self.left = None # pointer kiri (kosong)
        self.right = None # pointer kanan (kosong)

# Penjelasan alur fungsi Preorder
# Fungsi ini ngebaca pohon dari root ke bawah.
# Fungsi ini nyetak node tempat dia berdiri sekarang, menelusuri sampai habis semua anak di kiri, baru lanjut ke kanan.

def preorder(root):
    if root is not None: # pastikan node ada isinya
        print(root.data, end=" ") # cetak ke layar
        preorder(root.left) # telusuri cabang kiri
        preorder(root.right) # telusuri cabang kanan

# Penjelasan alur fungsi Tampil Struktur
# Fungsi ini cuma buat nggambar pohonnya di terminal pakai spasi tambahan, biar kelihatan mana parent dan child secara visual.

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: # jika posisi node tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # cetak dengan jarak spasi
        tampil_struktur(root.left, level + 1, "L") # cetak turunan kiri
        tampil_struktur(root.right, level + 1, "R") # cetak turunan kanan

# Penjelasan alur fungsi Rotate Right
# Ini kebalikan dari rotasi kiri. Dipakai pas pohon miring ke kiri. Anak di kiri ditarik naik jadi root utama, terus root yang lama diturunin paksa jadi anak kanannya dia.

# Implementasi Rotasi Kanan
def rotate_right(y):
    # y adalah root lama yang miring ke kiri
    x = y.left # x adalah child kiri y
    T2 = x.right # subtree kanan milik x disimpan sementara
    
    # Rotasi
    x.right = y # y menjadi child kanan dari x
    y.left = T2 # child kiri y diganti dengan T2
    
    return x # x menjadi root baru

if __name__ == '__main__':
    # Membuat tree yang tidak seimbang condong ke kiri:
    # 30 -> 20 -> 10
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)

    print("Preorder sebelum rotasi kanan:")
    preorder(root)

    print("\n\nStruktur sebelum rotasi kanan:")
    tampil_struktur(root)

    # Melakukan rotasi kanan pada root
    root = rotate_right(root)

    print("\nPreorder sesudah rotasi kanan:")
    preorder(root)

    print("\n\nStruktur sesudah rotasi kanan:")
    tampil_struktur(root)