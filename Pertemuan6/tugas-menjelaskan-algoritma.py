# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# =========================================================
# Penjelasan Insertion Sort (Ascending/Dari kecil ke besar)
# =========================================================

data = [9, 7, 15, 17, 5, 6]


def insertion_sort(arr):
    # melakukan iterasi array dari indeks 1/elemen 2 hingga akhir array
    for i in range(1, len(arr)):
        key = arr[i]  # elemen yang ingin kita evaluasi
        j = i-1  # elemen yang dibandingkan

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        # menentukan key di posisi yang tepat
        arr[j+1] = key

    return arr


print(f"data awal: {data}")
print(f"data tersortir (ascending): {insertion_sort(data)}")
