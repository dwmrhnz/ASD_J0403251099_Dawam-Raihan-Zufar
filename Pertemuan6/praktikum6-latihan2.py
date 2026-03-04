# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 2. Melengkapi potongan kode
# ===============================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key

    return data


"""
Soal
1. Lengkapi kondisi agar menjadi sorting ascending.
    jawaban: (kode di atas)

2. Ubah agar menjadi descending.
    jawaban: (kode di bawah)
"""


def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        while j >= 0 and data[j] < key:  # BERBEDA DI "<"
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key

    return data


# contoh
data = [2, 6, 7, 4, 5, 8]
print("Ascending: ", insertion_sort(data))
print("Descending: ", insertion_sort_descending(data))

"""
jawaban di line 26
"""