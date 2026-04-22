# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan BST
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data # simpan nilai
        self.left = None # pointer anak kiri (kosong)
        self.right = None # pointer anak kanan (kosong)

# Penjelasan alur fungsi Insert
# Fungsi ini buat masukin angka ke dalem pohon sesuai aturan. 
# Kalau pohonnya masih kosong banget, angka itu bakal jadi root-nya. 
# Tapi kalau sudah ada isi, dia bakal ngecek; kalau angka baru lebih gede dia ke kanan, kalau lebih kecil dia ke kiri.

def insert(root, data):
    if root is None: # jika posisi kosong
        return Node(data) # buat node baru di sini
    else:
        if root.data == data: # abaikan jika data duplikat
            return root
        elif root.data < data: # jika data baru lebih besar
            root.right = insert(root.right, data) # geser ke kanan
        else: # jika data baru lebih kecil
            root.left = insert(root.left, data) # geser ke kiri
    return root # kembalikan root terupdate

# Mengisi data BST
root = None 
data_list = [50, 30, 70, 20, 40, 60, 80] 

for data in data_list: 
    root = insert(root, data) # masukkan satu per satu
    print(data) 

print("BST berhasil dibuat") 


# ===============================================
# Latihan 2 : Traversal Inorder
# ===============================================

# Penjelasan alur fungsi Inorder
# Ini cara buat ngebaca atau nampilin isi pohon biar angkanya urut dari kecil ke besar.
# Caranya, dia bakal lari ke cabang paling kiri dulu, cetak datanya, baru pindah ke cabang kanan.

def inorder(root):
    if root: # pastikan node tidak kosong
        inorder(root.left) # telusuri cabang kiri
        print(root.data, end=" ") # cetak nilai node
        inorder(root.right) # telusuri cabang kanan


print("hasil Inorder: ") 
inorder(root) 


# ===============================================
# Latihan 3 : Search di BST
# ===============================================

# Penjelasan alur fungsi Search
# Fungsi ini buat nyari satu angka spesifik di dalem pohon, ada atau nggak.
# Dia bakal ngebandingin angka yang dicari sama node sekarang, kalau gak pas, dia milih mau nyari ke kiri atau ke kanan.

def search(root, key):
    if root is None: # mentok, data tidak ada
        return False

    if root.data == key: # cocok, data ditemukan
        return True

    if key < root.data: # target lebih kecil
        return search(root.left, key) # cari ke kiri
    else: # target lebih besar
        return search(root.right, key) # cari ke kanan


# Uji pencarian
key = 40 

if search(root, key): 
    print("\nData ditemukan") 
else: 
    print("\nData tidak ditemukan")