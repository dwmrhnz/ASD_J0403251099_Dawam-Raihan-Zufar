# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===========================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ===========================================

def biner(n, hasil=""):
    # Base caseL jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explorel : tambah '0'
    biner(n, hasil + "0")

    # Choose + Explorel : tambah '1'
    biner(n, hasil + "1")


biner(3)
