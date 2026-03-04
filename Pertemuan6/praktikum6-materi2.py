# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Insertion Sort (Ascending) dengan tracing
# ===============================================

def insertion_sort(data):
    # Melihat data awal
    print("Data awal:", data)
    print("=" * 50)

    # Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        key = data[i]  # simpan nilai yang disisipkan
        j = i-1  # index elemen terakhir di bagian kiri

        print("Iterasi ke-", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut): ", data[:i])
        print("Bagian kanan  (belum terurut): ", data[i:])

        # Geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # Sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan :", data)
        print("=" * 50)

    return data


data = [3, 7, 6, 8, 2, 1, 5, 4]
print(insertion_sort(data))
