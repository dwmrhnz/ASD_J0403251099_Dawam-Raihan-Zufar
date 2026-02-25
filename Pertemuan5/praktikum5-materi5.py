# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===========================================
# Contoh Bactracking 2: Kombinasi Biner dengan Batas '1' (pruning)
# ===========================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning : Jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return

    # Base case
    if len(hasil) == n:
        print(hasil)
        return

    # Pilih "0"
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih "1"
    biner_batas(n, batas, hasil + "1", jumlah_1)


biner_batas(4, 2)
