# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan BST
# ===============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    # Jika root kosong buat node baru
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        # jika data yang masuk lebih kecil dari root -> ke kri
        elif root.data < data:
            root.right = insert(root.right, data)
        # jika data yang masuk lebih besar dari root -> ke kri
        else:
            root.left = insert(root.left, data)
    return root


# Mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data)
    print(data)

print("BST berhasil dibuat")


# ===============================================
# Latihan 2 : Traversal Inorder
# ===============================================


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


print("hasil Inordeer: ")
inorder(root)

# ===============================================
# Latihan 3 : Search di BST
# ===============================================


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Uji pencarian
key = 40

if search(root, key):
    print("\nData ditemukan")
else:
    print("\nData tidak ditemukan")
