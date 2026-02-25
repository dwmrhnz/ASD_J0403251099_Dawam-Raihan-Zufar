# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ======================================================================
# Latihan 3: Mencari Nilai Maksimum
# Tujuan: Mengolah struktur data menggunakan rekursi.
# ======================================================================

def cari_maks(data, index=0):
    # BASE CASE
    # Jika pointer 'index' telah mencapai elemen terakhir dari struktur data list (indeks ke panjang list dikurangi 1), maka elemen tersebut dikembalikan sebagai nilai maksimum dari sub-masalah terkecil yang tersisa.
    if index == len(data) - 1:
        return data[index]
    
    # RECURSIVE CALL
    # Fungsi memanggil dirinya sendiri dengan menggeser pointer 'index' ke kanan (index + 1) untuk mencari nilai maksimum pada sisa elemen list berikutnya.
    maks_sisa = cari_maks(data, index + 1)
    
    # POST-RECURSIVE
    # Program membandingkan elemen pada 'index' saat ini dengan 'maks_sisa'
    if data[index] > maks_sisa:
        return data[index] # Mengembalikan elemen saat ini jika lebih besar.
    else:
        return maks_sisa   # Mempertahankan nilai maksimum dari elemen-elemen sebelumnya.


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))