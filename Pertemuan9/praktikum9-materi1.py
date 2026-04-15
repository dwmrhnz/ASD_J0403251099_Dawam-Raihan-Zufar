# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 1 : Membuat Node
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai data pada node
        self.left = None # child kiri
        self.right = None # child kanan

#Membuat Node root
root = Node("A") # membuat node root dengan nilai "A"

#Menampilkan isi node
print(f'Data pada root: {root.data}')
print(f'Child kiri root: {root.left}')
print(f'Child kanan root: {root.right}')

"""
Pembahasan:
Secara sederhana, langkah pertama untuk membuat Heap Tree (atau Binary Tree) adalah
menyiapkan blueprint atau cetakannya menggunakan **class Node**. Di dalam class ini,
kita pakai *constructor* **__init__** yang otomatis dieksekusi saat kita bikin node baru.
Fungsinya buat nyiapin tiga hal penting: **self.data** untuk menyimpan nilai aslinya,
serta **self.left** dan **self.right** sebagai *pointer* (penunjuk) ke *child* cabang kiri dan kanannya.
Nah, ketika kita menulis `root = Node("A")`, kita sebenarnya lagi bikin objek node pertama yang posisinya paling atas alias **root**,
dan kita isi datanya dengan "A". Karena node ini baru berdiri sendiri dan belum disambungin ke node mana-mana,
otomatis *pointer* cabang kiri dan kanannya masih kosong alias bernilai **None**. 
Intinya, kode ini adalah fondasi dasarnya. Buat jadi Heap Tree yang utuh,
nantinya kita tinggal nambahin node-node lain ke cabang kiri dan kanan si root ini sesuai dengan aturan *Max-Heap* atau *Min-Heap*.
"""