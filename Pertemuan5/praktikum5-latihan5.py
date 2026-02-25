# ======================================================================
# Studi Kasus: Generator PIN
# ======================================================================

def buat_pin(panjang, hasil=""):
    # BASE CASE
    # Memeriksa apakah panjang string solusi telah mencapai target 'panjang'.
    # Jika tercapai, cetak hasil dan lakukan return untuk inisiasi backtrack.
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # RECURSIVE
    # Melakukan perulangan pada domain nilai yang tersedia ("0", "1", "2").
    # Setiap iterasi menyebabkan pemanggilan rekursif untuk menyusun digit selanjutnya.
    for angka in ["0", "1", "2"]:
        #=============modifikasi============
        # Jika angka belum terdapat di dalam string hasil
        if angka not in hasil:
        #===================================
            buat_pin(panjang, hasil + angka)

buat_pin(3)


# ======================================================================
# DISKUSI: Bagaimana cara mencegah angka yang sama muncul berulang?
# ======================================================================
# Untuk mencegah pengulangan elemen, kita mengaplikasikan teknik "Pruning" (pemangkasan).
# Caranya dengan menambahkan validasi (conditional statement) sebelum melakukan pemanggilan rekursif.