# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# Representasi graph menggunakan adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    # Tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)
    
    # Tampilkan node yang sedang dikunjungi dengan format panah
    print(node, end=" -> ")
    
    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Lakukan DFS secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# Set kosong untuk menyimpan node yang sudah dikunjungi
visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)
print("Selesai")

# ==========================================
# JAWABAN PERTANYAAN ANALISIS - LATIHAN 2
# ==========================================
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# Jawaban: DFS di Python umumnya diimplementasikan menggunakan fungsi rekursif yang bekerja seperti struktur data Stack (LIFO).
# Saat menemukan tetangga baru, eksekusi untuk node saat ini ditunda sementara (masuk ke dalam Call Stack),
# dan fungsi langsung memanggil dirinya sendiri untuk mengeksplorasi tetangga baru tersebut.
# Ini memaksa penelusuran terus berlanjut ke bawah pada satu cabang sampai menemukan jalan buntu (dead end),
# sebelum melakukan backtrack (mundur) ke node sebelumnya.
#
# 2. Apa yang terjadi jika urutan neighbor diubah?
# Jawaban: Jalur yang dieksplorasi lebih dulu akan berubah, karena urutan pemanggilan rekursifnya berubah.
# Jika adjacency list untuk 'A' diubah menjadi ['C', 'B'], fungsi rekursif akan memanggil 'C' terlebih dahulu.
# DFS akan menelusuri seluruh cabang 'C' sampai ke ujung (F), baru kemudian mundur untuk menelusuri cabang 'B'.
#
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# Jawaban: 
# - Output DFS: A -> B -> D -> E -> C -> F -> Selesai. Eksekusi menelusuri secara vertikal/mendalam. Jalur kiri dihabiskan dulu (A-B-D), mundur ke B, pindah ke cabang E, mundur hingga ke A, lalu menyelesaikan jalur kanan (C-F).
# - Output BFS: A -> B -> C -> D -> E -> F -> Selesai. Eksekusi menelusuri secara horizontal/melebar per level. Node diproses murni berdasarkan tingkat kedekatannya dengan titik awal.