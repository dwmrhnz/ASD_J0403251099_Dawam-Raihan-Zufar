# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Implementasi BFS pada Graph
# ===============================================

# struktur data untuk mebuat antrean, kita gunakan dari library collections bawaan pyhton
from collections import deque

# represenatasi graph
graph = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": [],
    "e": [],
    "f": [],
    "g": []
}


def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran

    # Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    # variabel yang digunakn untuk menimpan node yang sudah diproses atau sudah dikunjungi
    visited = set()

    queue.append(start)

    # tandai node awal sbagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft()

        print(node, end=" ")

        # periksa smua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited:
                # tandai sbagai sudah dikunjungi
                visited.add(neighbor)
                # masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)


# menjalankan fungsi bfs
bfs(graph, "a")