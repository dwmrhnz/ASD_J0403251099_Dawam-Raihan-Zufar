# Praktikkum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca Seluruh Isi File
# -------------------------------------------------------#

file_path = "ASD_J0403251099_Dawam Raihan Zufar\Pertemuan1\data_mahasiswa.txt"

with open(file_path, "r", encoding="utf-8") as files:
    baca = files.read()
print(baca)

print("==Hasil Read==")
print("Tipe Data =", type(baca))
print("Jumlah Karakter =", len(baca))
print("Jumlah baris =", baca.count("\n")+1)

########## Membuia file per baris##########
print("==Membaca File per baris==")
jumlahBaris = 0
with open(file_path, "r", encoding="utf-8") as files:
    for baris in files:
        jumlahBaris += 1
        baris = baris.strip()
        print("Baris :", jumlahBaris)
        print("Isi", baris)


with open(file_path, "r", encoding="utf-8") as files:
    for baris in files:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print(f"NIM : {nim} | Nama : {nama} | Nilai : {nilai}")

########## Membaca File dan menyimpan di list##################
data_list = []
with open(file_path, "r", encoding="utf-8") as files:
    for baris in files:
        baris = baris.strip()
        nim, nama, kelas = baris.split(",")
        data_list.append([nim, nama, int(nilai)])

print("Data mahasiswa dalam list")
print(data_list)
print("panjang list :", len(data_list))
print("Data mahasiswa ke-1 :", data_list[0])

########## Membaca File dan menyimpan di dictionary##################
data_dict = {}
with open(file_path, "r", encoding="utf-8") as files:
    for baris in files:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "nama":  nama,
            "nilai": int(nilai)
        }
print(data_dict)
