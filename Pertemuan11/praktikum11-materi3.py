# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Implementasi DFS
# ===============================================

graph = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": [],
    "e": [],
    "f": [],
    "g": []
}

def dfs(graph, node, visited):
    #fungsi untuk melakukan penelusuran graph menggunakan DFS
    #graph : dictionary yang menyimpan graph
    #node : menyimpan node yang sedang dikunjungi
    #visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagfai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunnjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

#set visited
visited = set()

#Menjalankan dfs dari a
dfs(graph, "a", visited)