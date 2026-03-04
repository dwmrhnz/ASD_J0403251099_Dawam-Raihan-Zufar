# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 5. Melengkapi Fungsi Merge
# ===============================================

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

"""
Soal
1. Lengkapi kondisi agar menjadi ascending.
    jawaban: (kode di atas) 

2. Jelaskan fungsi result.extend()
    jawaban: mengganti dan menambahkan elemen yang sudah disortir tadi dari
    setiap sisi untuk dijadikan satu elemen yang utuh

"""