# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Penjelasan alur fungsi Insert
# Fungsi ini buat masukin data ke dalam pohon. Kalau datanya lebih kecil dia ngecek ke kiri,
# kalau lebih besar ngecek ke kanan sampai ketemu tempat yang kosong.

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root # kembalikan root terupdate

# Penjelasan alur fungsi Preorder
# Ini cara baca pohon dengan urutan:
# -cetak node sekarang dulu
# -telusuri semua cabang kiri
# -telusuri semua cabang kanan

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None: # pastikan node tidak kosong
        print(root.data, end=" ") # cetak nilai node saat ini
        preorder(root.left) # telusuri cabang kiri
        preorder(root.right) # telusuri cabang kanan

# Penjelasan alur fungsi Tampil Struktur
# Fungsi ini cuma buat nampilin bentuk pohon di layar biar kelihatan kayak hierarki.
# fungsi ini pakai spasi tambahan tiap turun level biar menjorok ke dalam.

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: # pastikan node tidak kosong
        print(" " * level + f"{posisi}: {root.data}") # cetak dengan spasi indentasi
        tampil_struktur(root.left, level + 1, "L") # cetak anak kiri
        tampil_struktur(root.right, level + 1, "R") # cetak anak kanan

if __name__ == '__main__':
    root = None
    
    # Data dimasukkan berurutan naik
    data_list = [10, 20, 30]
    
    for data in data_list:
        root = insert(root, data) # masukkan satu per satu
        
    print("Preorder BST:")
    preorder(root)
    
    print("\n\nStruktur BST:")
    tampil_struktur(root)

# 1. Tree condong ke kanan karena data dimasukkan berurutan naik.
# 2. Semakin panjang tree yang tidak seimbang, pencarian (search) akan makin lambat menyerupai Linked List berantai.