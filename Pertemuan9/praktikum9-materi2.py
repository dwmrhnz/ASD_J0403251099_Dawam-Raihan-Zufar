# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 2 : Membuat Binary search tree sederhana
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


#Menampilkan is node
print(f'Data pada root: {root.data}')
print(f'Child kiri root: {root.left.data}')
print(f'Child kanan root: {root.right.data}')
print(f'Child kiri dari B: {root.left.left.data}')
print(f'Child kanan dari B: {root.left.right.data}')
print(f'Child kiri dari C: {root.right.left.data}')
print(f'Child kanan dari C: {root.right.right.data}')


"""
Pembahasan:
kode ini menunjukkan cara merangkai node-node yang tadinya berdiri sendiri menjadi sebuah struktur pohon yang utuh dan bertingkat. 
Cara kerjanya mirip banget seperti membuat bagan silsilah keluarga. Kita mulai dari "A" sebagai pucuk tertinggi atau root.
Kemudian, kita langsung menyambungkan cabang kirinya dengan "B" dan cabang kanannya dengan "C" (ini disebut level 1).
Setelah itu, kita turun lagi ke level 2 dengan menambahkan anak pada "B" (yaitu "D" dan "E") serta pada "C" (yaitu "F" dan "G"). 
Untuk memanggil datanya, kita tinggal menelusuri jalurnya dari atas. Misalnya perintah `root.left.left.data`,
itu artinya kita menyuruh program mulai dari root, belok kiri ke B, lalu belok kiri lagi, dan sampailah kita di node yang menyimpan data "D".
"""