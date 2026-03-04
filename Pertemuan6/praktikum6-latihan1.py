# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Latihan 1. Memahami Kode Program (Insertion Sort)
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
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
    jawaban: karena indeks ke 0 sudah dianggap terurut, jadi kita
    mengambil elemen setelahnya untuk dibandingkan dan diletakkan di posisi yang tepat

2. Apa fungsi variabel key?
    jawaban: sebagai tempat penyimpanan sementara elemen yang sedang dicek

3. Mengapa digunakan while, bukan for?
    jawaban: karena jumlah iterasi atau pergeserannya tidak pasti 

4. Operasi apa yang terjadi di dalam while?
    jawaban: terjadi pergeseran elemen ke sebelah kanan untuk mengosongkan tempat yang akan diisi oleh key
"""
