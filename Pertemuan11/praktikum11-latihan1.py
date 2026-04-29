# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

from collections import deque

# Representasi graph
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    # Set digunakan untuk menyimpan node yang sudah dikunjungi
    visited = set()
    # Queue digunakan untuk menyimpan node yang akan diproses (prinsip FIFO)
    queue = deque([start])
    
    # Tandai node awal sebagai sudah dikunjungi
    visited.add(start)
    
    # Selama queue tidak kosong, proses terus berjalan
    while queue:
        # Ambil node paling depan dari queue
        node = queue.popleft()
        # Tambahkan spasi agar output lebih mudah dibaca
        print(node, end=" -> ")
        
        # Periksa semua tetangga dari node saat ini
        for neighbor in graph[node]:
            # Jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                # Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)
    print("Selesai")

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

# ==========================================
# JAWABAN PERTANYAAN ANALISIS - LATIHAN 1
# ==========================================
# 1. Node mana yang dikunjungi pertama?
# Jawaban: Node yang dikunjungi pertama adalah 'Rumah',
# karena node ini ditetapkan sebagai node awal (start) dan dimasukkan pertama kali ke dalam queue.
#
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# Jawaban: BFS mengunjungi node secara melebar (level per level).
# Node yang berada di level lebih rendah (lebih dekat dengan titik awal) akan selalu dimasukkan ke antrian dan
# diproses lebih dulu menggunakan prinsip FIFO (First In, First Out). Ini menjamin jalur yang ditemukan pertama kali adalah
# jalur dengan jumlah edge paling sedikit.
#
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Jawaban: Urutan kunjungan node pada level yang sama akan berubah. Jika adjacency list diubah menjadi
# 'Rumah': ['Toko', 'Sekolah'], maka 'Toko' akan diproses dan masuk antrian lebih dulu daripada 'Sekolah'.
# Akibatnya, tetangga dari 'Toko' (Pasar) juga akan dieksplorasi lebih dulu dibandingkan tetangga 'Sekolah' pada iterasi level berikutnya.