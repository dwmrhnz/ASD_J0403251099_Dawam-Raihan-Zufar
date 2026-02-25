# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ======================================================================
# Latihan 1: Rekursi Pangkat
# Tujuan: Memahami cara kerja Base Case dan Recursive Call
# ======================================================================

def pangkat(a, n):
    # BASE CASE
    # Logikanya adalah semua angka jika dipangkatkan 0 hasilnya adalah 1.
    # Jadi, kalau n sudah 0, berhenti dan kembalikan nilai 1.
    if n == 0:
        return 1
    
    # RECURSIVE CASE
    # Polanya: a^n = a * a^(n-1)
    # Kurangi n-nya (n-1) setiap kali memaanggil agar menyentuh angka 0 (base case).
    return a * pangkat(a, n - 1)


# Tracing Manual
# Misal: print(pangkat(2, 4))

# 1. pangkat(2, 4) -> return 2 * pangkat(2, 3) [Pending, nunggu hasil pangkat(2,3)]
# 2. pangkat(2, 3) -> return 2 * pangkat(2, 2) [Pending]
# 3. pangkat(2, 2) -> return 2 * pangkat(2, 1) [Pending]
# 4. pangkat(2, 1) -> return 2 * pangkat(2, 0) [Pending]
# 5. pangkat(2, 0) -> BASE CASE, n==0, return 1.

# Unwinding:
# - Hasil langkah 5 (angka 1) dikasih ke langkah 4: 2 * 1 = 2
# - Hasil langkah 4 (angka 2) dikasih ke langkah 3: 2 * 2 = 4
# - Hasil langkah 3 (angka 4) dikasih ke langkah 2: 2 * 4 = 8
# - Hasil langkah 2 (angka 8) dikasih ke langkah 1: 2 * 8 = 16

print(pangkat(2, 4)) # Output: 16