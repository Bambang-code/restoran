import json
import matplotlib.pyplot as plt
import os

# Fungsi untuk membaca data pesanan
def baca_pesanan(file_path):
    if not os.path.exists(file_path):
        print("File pesanan tidak ditemukan!")
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Gagal membaca file JSON.")
        return []

# Fungsi untuk menghasilkan laporan penjualan
def laporan_penjualan():
    file_path = "pesanan.json"
    data = baca_pesanan(file_path)

    if not data:
        print("Tidak ada data untuk ditampilkan!")
        return

    # Parsing data untuk grafik
    pesanan_items = data.get('pesanan', [])
    item_counts = {}
    for item in pesanan_items:
        item_counts[item] = item_counts.get(item, 0) + 1

    if not item_counts:
        print("Tidak ada pesanan yang dicatat!")
        return

    # Data untuk grafik
    items = list(item_counts.keys())
    counts = list(item_counts.values())

    # Membuat grafik
    plt.figure(figsize=(10, 6))
    plt.bar(items, counts, color='skyblue')
    plt.xlabel("Menu", fontsize=12)
    plt.ylabel("Jumlah Terjual", fontsize=12)
    plt.title("Laporan Penjualan", fontsize=16)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Tampilkan grafik
    plt.show()

# Memanggil fungsi untuk menampilkan laporan
if __name__ == "__main__":
    laporan_penjualan()
