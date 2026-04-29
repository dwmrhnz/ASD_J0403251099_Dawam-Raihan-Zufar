# ===========================================
# Nama  : Dawam Raihan Zufar
# NIM   : J0403251099
# Kelas : TPL B2
# ===========================================

# ===============================================
# Implementasi Dasar Graph
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