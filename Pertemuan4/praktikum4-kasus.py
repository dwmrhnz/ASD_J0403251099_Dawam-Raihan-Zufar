# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===========================================
# Studi kasus : Sistem Antrian Layan akademik
# Implementasi Queue =>
# Enqueue : Memindahkan pointer rear (menambah data baru dari belakang)
# Dequeue : Memindahkan pointer front (menghapus data dari depan)
# Dequeue
# Stack = Front -> C -> B -> A -> None
# Queue = Front -> A -> B -> C Rear
# ===========================================

class Node:
    def __init__(self, nim, nama):  # konstrukotr
        self.nim = nim
        self.nama = nama
        self.next = None  # pointer ke note berikutnya (awal=None)


class QueueAkademik:
    def __init__(self):
        self.front = None  # Node paling depan
        self.rear = None  # Node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue(self, nim, nama):
        # Menambah nim, nama di belakang (rear)
        nodeBaru = Node(nim, nama)
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
        # Menghapus data dari depan
        if self.is_empty():
            print("antrian kosong. Tidak ada mahasiswa yang dilayani")
        # 1) ambil data yang paling depan
        node_dilayani = self.front
        # 2) geser front ke node berikutnya
        self.front = self.front.next
        # 3) Jika setelah geser front menjadi none, maka queue kosong. Rear juga harus jadi none
        if self.front is None:
            self.rear = None
        return node_dilayani

    def tampilkan(self):
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1


def main():
    # instantiasi queue
    q = QueueAkademik()

    while True:
        print("===== Sistem Akademik =====")
        print("1. Tambah mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa Berhail ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilyani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai")
            break


if __name__ == "__main__":
    main()
