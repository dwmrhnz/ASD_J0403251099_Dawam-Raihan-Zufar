# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 3 : Membuat Traversal Preorder
# ===============================================

# Class Node adalah unit dasar pada Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi preorder : Root ==> left == > right

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menjalankan traversal preorder
print("Hasil Traversal Preorder")
preorder(root)

"""
Pembahasan:

Di latihan ketiga ini, kita belajar cara jalan-jalan atau mengunjungi setiap node di dalam tree menggunakan metode Preorder Traversal.
Kunci utama dari metode Preorder itu aturan urutannya: kunjungi titik saat ini (Root), lalu telusuri cabang Kiri sampai mentok, baru terakhir telusuri cabang Kanan.
Bintang utamanya ada di fungsi `preorder()`. Fungsi ini menggunakan teknik rekursi, alias memanggil dirinya sendiri secara berulang.
Saat dijalankan, program akan mengecek apakah node tersebut ada isinya. Kalau ada, datanya langsung dicetak ke layar.
Setelah itu, fungsi ini bakal otomatis menyuruh program untuk mengulang proses yang sama persis ke node sebelah kiri.
Kalau sebelah kiri sudah habis terjelajahi semua, barulah dia pindah untuk mengecek node sebelah kanan.
Kalau diaplikasikan ke silsilah tree yang kamu buat, alurnya bakal begini: Program mulai dari atas dan mencetak "A".
Terus dia belok kiri mencetak "B", dan turun ke kiri lagi mencetak "D". Karena "D" sudah mentok nggak punya anak, program mundur sedikit dan belok ke kanan buat mencetak "E".
Setelah urusan di cabang kiri root selesai semua, program baru pindah ke cabang kanan untuk mencetak "C", "F", dan terakhir "G".
Hasil akhirnya bakal keluar: A B D E C F G.
"""