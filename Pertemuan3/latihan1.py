class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

llist = LinkedList()
data_input = input("Masukan elemen ke Linked List: ")
data = data_input.strip().split()

for d in data:
    llist.insert_at_end(int(d))

print("Kondisi Linked List Awal:")
llist.display()

while True:
    print("Menu Hapus Node")
    print("1. Hapus")
    print("2. Exit")

    pilihan = int(input("Masukkan pilihan anda: "))
    if pilihan == 1:
        hapus = int(input("Masukan key yang ingin dihapus: "))
        llist.delete_node(hapus)
        llist.display()
        continue
    elif pilihan == 2:
        print("program selesai")
        break
        


