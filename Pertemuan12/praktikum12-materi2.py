# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# Praktikum 12 Graph II: Shortest Path
# ===========================================

# ===============================================
# Algoritma Bellman Ford
# =============================================== 

# Graph dengan bobot negatif untuk menguji kemampuan Bellman-Ford
graph = {
    'A': {'B': 5, 'C': 4}, # A ke B bobot 5, ke C bobot 4
    'B': {},                # B tidak ada tetangga keluar
    'C': {'B': -2}          # C ke B bobot negatif -2
}

def bellman_ford(graph, start): # Mendefinisikan fungsi Bellman-Ford
    # Inisialisasi awal jarak semua node sebagai tak hingga
    distances = {node: float('inf') for node in graph}
    distances [start] = 0 # Setel jarak titik awal adalah 0
    
    # Loop utama untuk relaksasi sebanyak (jumlah node - 1) kali
    for _ in range(len(graph) - 1):
        for node in graph: # Iterasi setiap node dalam graph
            # Iterasi setiap tetangga dan bobot dari node tersebut
            for neighbor, weight in graph [node].items():
                # Jika jarak asal valid dan rute baru lebih murah
                if distances[node] != float('inf') and distances[node] + weight < distances [neighbor]:
                    # Perbarui jarak minimum ke node tetangga
                    distances [neighbor] = distances [node] + weight
                    
    return distances # Mengembalikan hasil pemrosesan jarak

hasil = bellman_ford(graph, 'A') # Jalankan algoritma mulai dari node 'A'
print(hasil) # Tampilkan hasil akhir jarak terpendek