"""
========================================================
Praktikum 2 : Konsep ADT dan File handling (STUDI KASUS)
Latihan 1 : Mmebuat fungsi load data
========================================================
"""

nama_file = "ASD_J0403251099_Dawam Raihan Zufar\Pertemuan2\data_mahasiswa.txt"


data_dict = {}


def baca_data_mahasiswa(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict

# print("Data Mahasiswa: ", baca_data_mahasiswa(nama_file))
# print("Banyak Data: ", len(baca_data_mahasiswa(nama_file)))


"""
========================================================
Praktikum 2 : Konsep ADT dan File handling (STUDI KASUS)
Latihan 2 : Mmebuat fungsi menampilkan data
========================================================
"""


def tampilkan_data(data_dict):
    print("====== Daftar Mahasiwa ======")
    print(f"{'NIM':10} | {'Nama':<12} | {'Nilai':>5} ")
    print("-"*34)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama: <12} | {nilai:>5}")

# tampilkan_data(data_dict)


"""
========================================================
Praktikum 2 : Konsep ADT dan File handling (STUDI KASUS)
Latihan 3 : Mmebuat fungsi mencari data
========================================================
"""


def cari_data(datadict):
    print("=====================PENCARIAN DATA BERDASARKAN NIM=====================")
    nim_cari = input("Masukan NIM: ").strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']

        print("\n=========== Data Mahasiswa Ditemukan ============")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\n ==================Data Tidak Ditemukan==================")


# cari_data(data_dict)
"""
========================================================
Praktikum 2 : Konsep ADT dan File handling (STUDI KASUS)
Latihan 4 : Mmebuat fungsi update data
========================================================
"""


def update_nilai(data_dict):
    print("=====================UPDATE DATA=====================")
    nim = input("Masukan NIM: ").strip()
    if nim not in data_dict:
        print("NIM tidak ditemukan")
        return
    try:
        nilai_baru = int(input("Masukan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka, Update dibatalkan")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 smpai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = int(nilai_baru)
    print(f"Update berhasil. Nilai {nim} berubah menjadi {nilai_baru}")

# update_nilai(data_dict)


"""
========================================================
Praktikum 2 : Konsep ADT dan File handling (STUDI KASUS)
Latihan 5 : Mmebuat fungsi simpan data ke file txt
========================================================
"""


def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}")
# simpan_data(nama_file, data_dict)


"""
========================================================
Praktikum 2 : Konsep ADT dan File handling (STUDI KASUS)
Latihan 6: Mmebuat fungsi main
========================================================
"""


def main():
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n --- MENU DATA MAHASISWA ---")
        print("1. Tampilkan ")
        print("2. cari")
        print("3. update")
        print("4. simpan")
        print("0. Keluar")

        pilihan = int(input("Masukan pilihan : "))

        if pilihan == 1:
            tampilkan_data(data_dict)
        elif pilihan == 2:
            cari_data(data_dict)
        elif pilihan == 3:
            update_nilai(data_dict)
        elif pilihan == 4:
            simpan_data(nama_file, data_dict)
        elif pilihan == 0:
            print("Program selesai")
            break


if __name__ == "__main__":
    main()
