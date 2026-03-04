# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Merge Sort (Ascending) dengan iterasi
# ===============================================

def merge_sort(data, depth = 0):
    indent = "----" * depth #indentasi berdasarkan level rekursif
    print(f"{indent}merge_sort({data})")

    # Base case: jika elemen kurang dari atau sama dengan 1, data sudah dianggap terurut
    if len(data) <= 1:
        return data

    # Mencari titik tengah data
    mid = len(data) // 2
    
    # Membagi data menjadi dua bagian: kiri dan kanan
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    print(f"{indent}divide -> left = {left} | right = {right}")

    # Memanggil fungsi itu sendiri (rekursi) untuk memecah setiap bagian
    left = merge_sort(left, depth+1)
    right = merge_sort(right,depth+1)
    # Menggabungkan bagian yang sudah diurutkan
    merged_data = merge(left, right)
    print(f"{indent}merged -> {merged_data}")
    
    # Menggabungkan bagian yang sudah diurutkan dengan fungsi helper
    return merged_data


def merge(left, right):
    result = []
    i = j = 0

    # Membandingkan elemen dari bagian kiri dan kanan, lalu memasukkan yang lebih kecil
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Memasukkan sisa elemen jika salah satu sisi (kiri atau kanan) sudah habis
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Contoh penggunaan:
data = [13, 7, 28, 5, 19, 36, 4]
data_terurut = merge_sort(data)
print("Data awal:", data)
print("Data terurut:", data_terurut)