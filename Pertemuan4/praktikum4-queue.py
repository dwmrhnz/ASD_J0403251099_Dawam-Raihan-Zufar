#===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
#===========================================

#===========================================
#Implementasi Dasar : Queue berbasis Linked List
#===========================================

class Node:
    def __init__(self, data): #konstrukotr
        self.data = data #menyimpan nilai /data
        self.next = None #pointer ke note berikutnya (awal=None)

#Queue dengan 2 pointer : front rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        #Menambah data di belakang (rear)
        nodeBaru = Node(data)
        # jika queue kosong front and rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # Jika queue tidak kosong:
        # Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        # Rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        #Menghapus data dari depan

        # 1) ambil data yang paling depan
        data_dihapus = self.front.data
        # 2) geser front ke node berikutnya
        self.front = self.front.next
        # 3) Jika setelah geser front menjadi none, maka queue kosong. Rear juga harus jadi none
        if self.front is None:
            self.rear = None
        return data_dihapus
    def tampilkan(self):
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")



# INSTANSTIASI OBJEK CLASS QUEUEll
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()