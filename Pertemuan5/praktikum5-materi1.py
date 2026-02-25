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
    # base case: berhenti ketika n = 0
    if n == 0 or n == 1:
        return 1
    # recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n*faktorial(n-1)


print(faktorial(5)) #output: 120