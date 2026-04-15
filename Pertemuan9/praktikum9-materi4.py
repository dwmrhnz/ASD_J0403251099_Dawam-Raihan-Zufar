# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 4 : Membuat Traversal Inorder
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# membuat fungsi inorder : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

## Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menjalankan traversal inorder
print("Hasil Traversal Inorder")
inorder(root)

"""
Pembahasan:
Kode ini menerapkan metode Inorder Traversal untuk menelusuri node pada tree. Aturan eksekusi metode Inorder selalu mengikuti pola urutan: menelusuri cabang kiri hingga akhir, mencetak data pada node saat ini, lalu menelusuri cabang kanan.

Fungsi inorder pada kode ini bekerja menggunakan pendekatan rekursif. Saat fungsi dijalankan berawal dari root A, program tidak langsung mencetak A, melainkan memanggil kembali fungsi tersebut untuk menelusuri cabang sebelah kiri hingga mencapai node paling ujung bawah, yaitu D. 

Setelah node D dicetak, alur program bergerak naik untuk mencetak parent-nya yaitu B, kemudian bergeser memeriksa cabang kanan B, yaitu E. Ketika seluruh struktur di sebelah kiri root utama selesai diproses (menghasilkan D B E), barulah nilai root A dicetak. Selanjutnya, program menerapkan langkah yang sama persis untuk menyelesaikan sisa node di sebelah kanan root A. Keseluruhan proses penelusuran ini akan menghasilkan output akhir: D B E A F C G.
"""