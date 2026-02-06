# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File.txt)
#
# Nama : Dawam Raihan Zufar
# NIM : J0403251099
# Kelas : TPL B2
# ==========================================================

# -------------------
# Konstanta nama file
# -------------------

NAMA_FILE = "Pertemuan2/stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarnag,NamaBarang,Stok

    Output:
    - stok_dick (dictionary)
    - key = kode_barang
    - value = {"nama": nama_barang, "stok": stok_int"}
    """
    stok_dict = {}

    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            stok_dict[kode] = {
                "nama": nama,
                "stok": int(stok)
            }
    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")
    pass

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    if not stok_dict:
        print("\nStok Barang Kosong. Silahkan Tambah Barang Baru.")
    else:
        print("\n=========== STOK BARANG ===========")
        print(f"{'Kode':10} | {'Nama':<12} | {'Stok':>5} ")
        print("-"*34)

        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            print(f"{kode:<10} | {nama: <12} | {stok:>5}")
    pass

# ------------------------------------
# Fungsi: Cari barang berdasarkan kode
# ------------------------------------

def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """

    print("================ PENCARIAN BARANG BERDASARKAN KODE ================")
    kode = input("Masukan kode: ").strip()
    if kode in stok_dict:
        nama = stok_dict[kode]['nama']
        stok = stok_dict[kode]['stok']

        print("\nStok Barang Ditemukan")
        print(f"Kode : {kode}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("\nStok Barang Tidak Ditemukan")
    pass

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------

def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan")
        return
    nama = input("Masukkan nama barang: ").strip()

    
    stok_awal = int(input("Masukkan stok awal barang: "))

    if not stok_awal < 0:
        stok_dict[kode] = {
                "nama": nama,
                "stok": int(stok_awal)
        }
    else:
        print("Stok awal tidak boleh negatif")
    pass

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------

def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    print("============= UPDATE STOK =============")
    kode = input("Masukan kode yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Kode tidak ditemukan")
        return
    nama = stok_dict[kode]["nama"]
    stok_lama = stok_dict[kode]["stok"]
    stok_baru = stok_lama
    print(f"Nama barang: {nama}")
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    try:
        pilihan = int(input("Masukkan pilihan (1/2): "))
        if not pilihan in [1,2]:
            print("Input salah. Masukkan angka pilihan 1 atau 2.")
            return
        jumlah = int(input("Masukkan total yang ingin dijumlah: "))
    except ValueError:
        print("Masukkan angka")
        return

    if pilihan == 1:
        stok_baru += jumlah
    elif pilihan == 2:
        stok_baru -= jumlah

    if stok_baru < 0:
        print("Stok menjadi negatif, update stok dibatalkan.")
        return
    else:
        stok_dict[kode]["stok"] = stok_baru

    print(f"Update berhasil. Stok {kode}_{nama} berubah dari {stok_lama} menjadi {stok_baru}")

# -------------------------------
# Program Utama
# -------------------------------

def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)
    
    while True:
        print("\n --- MENU STOK KANTIN ---")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Kode")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Simpan ke File")
        print("0. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            "Masukkan angka"

        if pilihan == 1:
            tampilkan_semua(stok_barang)
        elif pilihan == 2:
            cari_barang(stok_barang)
        elif pilihan == 3:
            tambah_barang(stok_barang)
        elif pilihan == 4:
            update_stok(stok_barang)
        elif pilihan == 5:
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == 0:
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi. (0-5)")

# Menjalankan program utama
if __name__ == "__main__":
    main()
