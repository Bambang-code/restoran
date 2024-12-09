import matplotlib.pyplot as plt

# Data global untuk penyimpanan
menu = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 20000},
    {"id": 2, "nama": "Ayam Bakar", "harga": 25000},
    {"id": 3, "nama": "Es Teh", "harga": 5000}
]
pesanan = []
laporan_penjualan = []

# Data login
users = {
    "kasir": {"username": "kasir1", "password": "kasir123"},
    "admin": {"username": "admin1", "password": "admin123"},
    "owner": {"username": "owner1", "password": "owner123"}
}

# Fungsi login
def login(role):
    print(f"=== Login {role.capitalize()} ===")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == users[role]["username"] and password == users[role]["password"]:
        print("Login berhasil!")
        return True
    else:
        print("Login gagal! Username atau password salah.")
        return False

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
        print("1. Pelanggan (tanpa login)")
        print("2. Kasir (login diperlukan)")
        print("3. Admin (login diperlukan)")
        print("4. Owner (login diperlukan)")
        print("5. Keluar")
        pilihan = int(input("Pilih menu: "))
        
        if pilihan == 1:
            pelanggan()
        elif pilihan == 2:
            if login("kasir"):
                kasir()
        elif pilihan == 3:
            if login("admin"):
                admin()
        elif pilihan == 4:
            if login("owner"):
                owner()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program utama
if __name__ == "__main__":
    main()
