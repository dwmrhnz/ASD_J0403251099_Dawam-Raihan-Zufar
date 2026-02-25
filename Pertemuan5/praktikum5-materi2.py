#===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
#===========================================

#===========================================
# Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# 1 - 2 - 3
# Keluar
#===========================================

def hitung(n):
    #base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)
    hitung(n-1) #recursive case
    print("Keluar", n)
print("======PROGRAM TRACING======")
hitung(5)