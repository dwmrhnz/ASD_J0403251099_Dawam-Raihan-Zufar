#===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
#===========================================

#===========================================
# Materi Rekursif : Menjumlahkan Elemen List
#===========================================

def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0

    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index+1)

print("========Program Jumlah data list===========")
print(jumlah_list([2,3,4,5,6,8])) # output 28 