# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 5 : Membuat Traversal Postorder
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# membuat fungsi postorder : left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

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

# Menjalankan traversal postorder
print("Hasil Traversal postorder")
postorder(root)

"""
Pembahasan:
Pada latihan kelima ini, kode menerapkan metode Postorder Traversal. Sesuai dengan aturan dasarnya, metode ini memprioritaskan penelusuran pada kedua cabang anak terlebih dahulu sebelum mengeksekusi atau mencetak nilai pada node induk. Secara sederhana, urutan pergerakannya selalu memproses cabang kiri, lalu cabang kanan, dan terakhir root.

Fungsi rekursif pada kode ini akan menginstruksikan program untuk mengabaikan pencetakan dan turun langsung ke cabang paling kiri bawah. Saat tiba di node D dan mendapati tidak ada cabang lagi, program akan mencetak nilainya. Sebelum mencetak induknya yaitu node B, program diwajibkan untuk memproses cabang kanan dari B terlebih dahulu, yaitu node E. Setelah kedua anak tersebut selesai dicetak, barulah nilai induk B dimunculkan.

Pola penyelesaian dari bawah ke atas ini juga diterapkan secara identik pada sisi kanan tree. Program akan menelusuri ke bawah untuk mencetak node F, lalu berpindah ke node G, dan dilanjutkan dengan mencetak induk mereka yaitu node C. Karena seluruh komponen di cabang kiri dan kanan sudah selesai diproses secara menyeluruh, barulah nilai puncak atau root utama A dicetak pada bagian paling akhir. Proses ini akan menghasilkan urutan output berupa D E B F G C A.
"""