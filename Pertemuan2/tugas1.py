file_path = "ASD_J0403251099_Dawam Raihan Zufar\Pertemuan2\stok_barang.txt"

stok_dict = {}


def baca_stok(file):
    with open(file, "r", encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            stok_dict[kode] = {
                "nama": nama,
                "stok": int(stok)
            }
        return stok_dict


def tampilkan_stok(dict):
    print("====== Daftar Mahasiwa ======")
    print(f"{'Kode':10} | {'Nama':<12} | {'Stok':>5} ")
    print("-"*34)

    for kode in sorted(dict.keys()):
        nama = dict[kode]["nama"]
        stok = dict[kode]["stok"]
        print(f"{kode:<10} | {nama: <12} | {stok:>5}")


def cari_kode(dict):
    print("=====================PENCARIAN BARANG BERDASARKAN KODE=====================")
    kode_cari = input("Masukan kode: ").strip()
    if kode_cari in dict:
        nama = dict[kode_cari]['nama']
        stok = dict[kode_cari]['stok']

        print("\n=========== Stok Barang Ditemukan ============")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("\n ==================Stok Barang Tidak Ditemukan==================")


def update_stok(dict):
    print("=====================UPDATE STOK=====================")
    kode = input("Masukan kode: ").strip()
    if kode not in dict:
        print("Kode tidak ditemukan")
        return
    try:
        stok_baru = int(input("Masukan Stok baru: ").strip())
    except ValueError:
        print("Stok harus berupa angka, Update dibatalkan")
        return

    stok_lama = dict[kode]["stok"]
    dict[kode]["stok"] = int(stok_baru)
    print(
        f"Update berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")


def simpan(file, dict):
    with open(file, "w", encoding="utf-8") as f:
        for kode in sorted(dict.keys()):
            nama = dict[kode]["nama"]
            stok = dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}")


def main():
    baca_stok(file_path)
    while True:
        print("\n --- MENU DATA MAHASISWA ---")
        print("1. Tampilkan Barang")
        print("2. Cari Barang")
        print("3. Update Stok Barang")
        print("4. Simpan")
        print("0. Keluar")

        pilihan = int(input("Masukan pilihan : "))

        if pilihan == 1:
            tampilkan_stok(stok_dict)
        elif pilihan == 2:
            cari_kode(stok_dict)
        elif pilihan == 3:
            update_stok(stok_dict)
        elif pilihan == 4:
            simpan(file_path, stok_dict)
        elif pilihan == 0:
            print("Program selesai")
            break


if __name__ == "__main__":
    main()
