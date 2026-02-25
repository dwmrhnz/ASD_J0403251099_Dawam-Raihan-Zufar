# ===========================================
# Nama  : Dawam Raihan ZUfar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ======================================================================
# Latihan 2: Tracing Rekursi
# Tujuan: Memahami alur masuk dan keluar fungsi pada proses rekursi.
# ======================================================================

def countdown(n):
    # BASE CASE
    # Jika nilai n mencapai 0, program akan mencetak "Selesai" dan menghentikan eksekusi fungsi saat ini menggunakan perintah 'return'.
    if n == 0:
        print("Selesai")
        return
    
    # PRE-RECURSIVE
    # Status nilai variabel n dari pemanggilan saat ini dicetak.
    print("Masuk:", n)
    
    # RECURSIVE CALL
    # Fungsi memanggil dirinya sendiri dengan argumen yang dikurangi 1 (n - 1).
    countdown(n - 1)
    
    # POST-RECURSIVE
    # Instruksi ini hanya akan dieksekusi setelah pemanggilan rekursif (countdown(n-1)) mencapai base case dan dikembalikan (return).
    print("Keluar:", n)

# Inisialisasi pemanggilan fungsi
countdown(3)


# ======================================================================
# DISKUSI: Mengapa output 'Keluar' muncul terbalik?
# ======================================================================
# Penjelasan Alur Eksekusi:
# Ketika program dijalankan dengan countdown(3), proses yang terjadi di tumpukan memori (Stack) menerapkan prinsip LIFO (Last In, First Out).

# Fase Masuk
# 1. Eksekusi countdown(3): Cetak "Masuk: 3" -> Panggil countdown(2). (Instruksi Cetak "Keluar: 3" ditunda di Stack).
# 2. Eksekusi countdown(2): Cetak "Masuk: 2" -> Panggil countdown(1). (Instruksi Cetak "Keluar: 2" ditunda di Stack).
# 3. Eksekusi countdown(1): Cetak "Masuk: 1" -> Panggil countdown(0). (Instruksi Cetak "Keluar: 1" ditunda di Stack).
# 4. Eksekusi countdown(0): BASE CASE terpenuhi. Cetak "Selesai" -> 'return'
#
# Fase Keluar / Undwinding
# 5. Kontrol kembali ke countdown(1): Eksekusi sisa instruksi -> Cetak "Keluar: 1", lalu selesai.
# 6. Kontrol kembali ke countdown(2): Eksekusi sisa instruksi -> Cetak "Keluar: 2", lalu selesai.
# 7. Kontrol kembali ke countdown(3): Eksekusi sisa instruksi -> Cetak "Keluar: 3", lalu eksekusi program utama selesai.