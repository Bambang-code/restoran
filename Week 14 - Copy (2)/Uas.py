import matplotlib.pyplot as plt

# Data global untuk penyimpanan
menu = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 20000},
    {"id": 2, "nama": "Ayam Bakar", "harga": 25000},
    {"id": 3, "nama": "Es Teh", "harga": 5000}
]
pesanan = []
laporan_penjualan = []

# Fungsi untuk pelanggan
def pelanggan():
    print("=== Menu Pelanggan ===")
    nomor_meja = input("Masukkan nomor meja: ")
    print("Daftar Menu:")
    for item in menu:
        print(f"{item['id']}. {item['nama']} - Rp{item['harga']}")
    
    pilihan = int(input("Pilih menu (masukkan ID): "))
    jumlah = int(input("Masukkan jumlah: "))
    for item in menu:
        if item["id"] == pilihan:
            pesanan.append({"meja": nomor_meja, "menu": item, "jumlah": jumlah})
            print(f"Pesanan {item['nama']} untuk meja {nomor_meja} berhasil dibuat.")
            break

# Fungsi untuk kasir
def kasir():
    print("=== Menu Kasir ===")
    print("Pesanan Saat Ini:")
    total = 0
    for p in pesanan:
        subtotal = p["menu"]["harga"] * p["jumlah"]
        total += subtotal
        print(f"Meja {p['meja']}: {p['menu']['nama']} x {p['jumlah']} = Rp{subtotal}")
    
    print(f"Total: Rp{total}")
    metode_bayar = input("Metode Pembayaran (Tunai/Kartu/QRIS): ")
    laporan_penjualan.append({"total": total, "metode": metode_bayar})
    print("Pembayaran berhasil!")

# Fungsi untuk admin
def admin():
    print("=== Menu Admin ===")
    print("1. Tambah Menu")
    print("2. Hapus Menu")
    print("3. Update Menu")
    pilihan = int(input("Pilih menu: "))
    
    if pilihan == 1:
        nama = input("Masukkan nama menu: ")
        harga = int(input("Masukkan harga menu: "))
        menu.append({"id": len(menu) + 1, "nama": nama, "harga": harga})
        print(f"Menu {nama} berhasil ditambahkan.")
    elif pilihan == 2:
        hapus_id = int(input("Masukkan ID menu yang ingin dihapus: "))
        menu[:] = [item for item in menu if item["id"] != hapus_id]
        print("Menu berhasil dihapus.")
    elif pilihan == 3:
        update_id = int(input("Masukkan ID menu yang ingin diupdate: "))
        for item in menu:
            if item["id"] == update_id:
                item["nama"] = input("Masukkan nama baru: ")
                item["harga"] = int(input("Masukkan harga baru: "))
                print("Menu berhasil diupdate.")
                break

# Fungsi untuk owner
def owner():
    print("=== Laporan Penjualan ===")
    total_penjualan = sum([item["total"] for item in laporan_penjualan])
    print(f"Total Penjualan: Rp{total_penjualan}")
    
    # Grafik penjualan berdasarkan metode pembayaran
    metode = [item["metode"] for item in laporan_penjualan]
    metode_unik = list(set(metode))
    jumlah_metode = [metode.count(m) for m in metode_unik]
    
    plt.bar(metode_unik, jumlah_metode, color='skyblue')
    plt.title("Laporan Penjualan Berdasarkan Metode Pembayaran")
    plt.xlabel("Metode Pembayaran")
    plt.ylabel("Jumlah Transaksi")
    plt.show()

# Program utama
def main():
    while True:
        print("=== Sistem Restoran ===")
        print("1. Pelanggan")
        print("2. Kasir")
        print("3. Admin")
        print("4. Owner")
        print("5. Keluar")
        pilihan = int(input("Pilih menu: "))
        
        if pilihan == 1:
            pelanggan()
        elif pilihan == 2:
            kasir()
        elif pilihan == 3:
            admin()
        elif pilihan == 4:
            owner()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program utama
if __name__ == "__main__":
    main()
