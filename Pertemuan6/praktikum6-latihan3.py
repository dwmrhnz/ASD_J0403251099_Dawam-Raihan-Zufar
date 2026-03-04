# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 3. Tracing Insertion Sort
# ===============================================

def insertion_sort_tracing(data):
    print("Data awal:", data)
    print("=" * 50)

    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        print("Iterasi ke-", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut): ", data[:i])
        print("Bagian kanan  (belum terurut): ", data[i:])

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("=" * 50)

    return data


data = [5, 2, 4, 6, 1, 3]
print(insertion_sort_tracing(data))

"""
Soal:
1. Tuliskan isi list setelah iterasi i=1
    jawaban = [2, 5, 4, 6, 1, 3]

2. Tuliskan isi list setelah iterasi i=3
    jawaban = [2, 4, 5, 6, 1, 3]
    
3. Berapa kali pergeseran terjadi pada iterasi i=4?
    jawaban = 4 kali
"""
