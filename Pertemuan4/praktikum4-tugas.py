# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ====================================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ====================================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None  # Pointer untuk menunjuk ke pelanggan berikutnya


class QueueBengkel:
    def __init__(self):
        # Menginisialisasi pointer front (depan) dan rear (belakang)
        self.front = None
        self.rear = None

    def enqueue(self, no, nama, servis):
        # Membuat node baru berisi data pelanggan
        new_node = Node(no, nama, servis)

        # Jika antrian kosong, front dan rear akan menunjuk ke node baru
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            print(f"> Berhasil menambahkan pelanggan {nama} ke antrian.")
            return

        # Jika tidak kosong, tambahkan node baru di belakang antrian (rear.next)
        self.rear.next = new_node
        # Pindahkan pointer rear ke node yang paling baru masuk tersebut
        self.rear = new_node
        print(f"> Berhasil menambahkan pelanggan {nama} ke antrian.")

    def dequeue(self):
        # Jika antrian kosong, tidak ada yang bisa dilayani
        if self.front is None:
            print("> Antrian saat ini sedang kosong. Tidak ada pelanggan untuk dilayani.")
            return

        # Menyimpan data pelanggan yang akan dilayani (selalu yang ada di front/depan)
        pelanggan_dilayani = self.front

        # Menggeser pointer front ke node berikutnya (memutus/menghapus pelanggan pertama dari antrian)
        self.front = self.front.next

        # Jika setelah digeser front menjadi None, berarti antrian sudah habis/kosong.
        # Maka rear juga harus dikosongkan (di-set None)
        if self.front is None:
            self.rear = None

        print(
            f"> Memproses pelayanan... Selesai melayani Pelanggan [No: {pelanggan_dilayani.no} | Nama: {pelanggan_dilayani.nama} | Servis: {pelanggan_dilayani.servis}]")

    def tampilkan(self):
        # Jika antrian kosong
        if self.front is None:
            print("> Antrian saat ini sedang kosong.")
            return

        print("\n--- Daftar Antrian Bengkel ---")
        # Mulai traversal (penelusuran) dari node terdepan (front)
        current = self.front
        urutan = 1

        # Selama node saat ini ada (tidak None), cetak datanya lalu geser
        while current is not None:
            print(
                f"{urutan}. No: {current.no} | Nama: {current.nama} | Servis: {current.servis}")
            # Geser pointer current ke node selanjutnya dalam Linked List
            current = current.next
            urutan += 1
        print("------------------------------")


def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("> Terima kasih telah menggunakan Sistem Antrian Bengkel.")
            break

        else:
            print("> Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
