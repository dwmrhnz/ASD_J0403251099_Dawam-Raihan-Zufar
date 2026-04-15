# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 6 : Struktur Organisasi Perusahaan
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Membuat  Tree struktur organisasi
root = Node("Direktur")

# Membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.left = Node("Staff 3")


# Menjalankan traversal preorder
print("Struktur organisasi  (preorder)")
preorder(root)

"""
Pembahasan:
Latihan keenam ini sangat menarik karena kita mulai mengaplikasikan konsep tree ke dalam studi kasus dunia nyata, yaitu membangun hierarki struktur organisasi perusahaan. Puncak hierarki atau root pada pohon ini diisi oleh Direktur. Di bawahnya terdapat cabang pertama yang ditempati oleh Manajer A di divisi kiri dan Manajer B di divisi kanan. Struktur ini kemudian berlanjut ke bawah dengan menambahkan staf sebagai bawahan langsung dari masing-masing manajer.

Untuk menampilkan susunan struktur tersebut, program memanggil kembali metode Preorder. Alur penelusuran ini sangat cocok untuk hierarki karena akan selalu mencetak jabatan atasan terlebih dahulu sebelum mendata bawahannya. Program pertama kali akan mencetak jabatan Direktur, lalu masuk ke divisi Manajer A dan mendata seluruh staf di bawahnya yaitu Staff 1 dan Staff 2. Setelah divisi kiri selesai didata secara menyeluruh, barulah program bergeser ke divisi kanan untuk mencetak Manajer B beserta bawahannya yaitu Staff 3. Hasil akhirnya akan tampil berurutan: Direktur, Manajer A, Staff 1, Staff 2, Manajer B, lalu Staff 3.
"""