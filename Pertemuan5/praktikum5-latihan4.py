# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ======================================================================
# Latihan 4: Kombinasi Huruf
# Tujuan: Implementasi pola choose dan explore
# ======================================================================

def kombinasi(n, hasil=""):
    # BASE CASE
    # Memeriksa apakah panjang string ('hasil') telah memenuhi target 'n'.
    # Jika terpenuhi, solusi dicetak dan aliran program kembali ke node sebelumnya.
    if len(hasil) == n:
        print(hasil)
        return

    # RECURSIVE
    # Baris pertama mengeksplorasi penambahan karakter "A", baris kedua untuk karakter "B".
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


kombinasi(2)

# ======================================================================
# Diskusi: Jumlah Kombinasi yang dihasilkan
# ======================================================================
# Jumlah kombinasi mengikuti rumus perpangkatan r^n (r = jumlah opsi, n = panjang).
# Dengan 2 opsi karakter ('A', 'B') dan n=2, maka total node yang terbentuk adalah 2^2 = 4 kombinasi (AA, AB, BA, BB).
