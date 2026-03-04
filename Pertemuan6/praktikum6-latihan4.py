# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 4. Memahami Kode Program (Merge Sort)
# ===============================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


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
1. Apa yang dimaksud dengan base case?
    jawaban: kondisi di mana fungsi tidak akan memanggil dirinya sendiri lagi dan langsung memberikan hasil
    
2. Mengapa fungsi memanggil dirinya sendiri?
    jawaban: untuk membagi data sebelah kiri dan kanan secara berulang
    
3. Apa tujuan fungsi merge()?
    jawaban: mengurutkan data masing2 di sebelah kir dan kanan kemudian 
    menggabungkan data sebelah kiri dan kanan untuk dijadikan data yang tersortir utuh.
"""
