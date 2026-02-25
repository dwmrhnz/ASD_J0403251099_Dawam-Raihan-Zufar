# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===========================================
# Materi Rekursif : Faktorial
# Recursive case => 3! 3 x 2 x 1
# base case => 0 berhenti
# ===========================================

def faktorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    return n*faktorial(n-1)


print(faktorial(5))
