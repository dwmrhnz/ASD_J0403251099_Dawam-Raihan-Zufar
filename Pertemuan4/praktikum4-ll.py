#===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
#===========================================

#===========================================
#Implementasi Dasar : Node pada Linked List
#===========================================

# Membuat class Node
class Node:
    def __init__(self, data):
        self.data = data #menyimpan data
        self.next = None #pointer ke node berikutnya (awal = None)

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Mengubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menelususri dari Head -> None
current = head
while current is not None:
    print(current.data)
    current = current.next
print("==========List Baru==========")

#===========================================
# Implementasi Dasr : Linked List  - Insert Awal
#===========================================

class LinkedList:
    def __init__(self):
        self.head= None #awalnya kosong

    def insert_awal(self, data): #push dala stack
        #1) Buat node baru
        nodeBaru = Node(data) #panggil  class node
        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head
        # 3) head pindah ke node baru
        self.head = nodeBaru
    
    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggesr head ke node slanjutnya
        self.head = self.head.next
        print("Node yang dihapus adalah:", data_terhapus)

    def tampilkan(self): #implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()