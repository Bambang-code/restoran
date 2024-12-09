# Simulasi sistem manajemen restoran

# Data awal
menu = [
    {"nama": "Nasi Goreng", "harga": 20000},
    {"nama": "Mie Goreng", "harga": 18000},
    {"nama": "Es Teh", "harga": 5000},
]

pegawai = [{"username": "admin", "password": "admin123", "role": "admin"}]
penjualan = []
metode_pembayaran = ["Tunai", "Kartu", "QRIS"]


def menu_pelanggan():
    print("\n=== Menu Pelanggan ===")
    meja = input("Masukkan nomor meja: ")
    pesanan = []
    total = 0

    print("\nMenu:")
    for i, item in enumerate(menu):
        print(f"{i + 1}. {item['nama']} - Rp{item['harga']}")

    while True:
        pilih = input("Pilih menu (nomor) atau ketik 'selesai': ")
        if pilih.lower() == "selesai":
            break
        elif pilih.isdigit() and 1 <= int(pilih) <= len(menu):
            pesanan.append(menu[int(pilih) - 1]["nama"])
            total += menu[int(pilih) - 1]["harga"]
            print(f"{menu[int(pilih) - 1]['nama']} ditambahkan ke pesanan.")
        else:
            print("Pilihan tidak valid.")

    print("\nPesanan Anda:", pesanan)
    print("Total harga: Rp", total)
    kritik = input("Masukkan kritik/saran: ")
    penjualan.append({"meja": meja, "pesanan": pesanan, "total": total})
    print("Terima kasih atas pesanan Anda!")


def menu_kasir():
    print("\n=== Menu Kasir ===")
    print("Daftar penjualan:")
    for i, transaksi in enumerate(penjualan):
        print(f"{i + 1}. Meja {transaksi['meja']} - Total: Rp{transaksi['total']}")

    metode = input(f"Pilih metode pembayaran ({', '.join(metode_pembayaran)}): ")
    if metode in metode_pembayaran:
        print("Pembayaran berhasil menggunakan", metode)
    else:
        print("Metode pembayaran tidak valid.")


def menu_admin():
    print("\n=== Menu Admin ===")
    print("1. Tambah menu")
    print("2. Hapus menu")
    print("3. Ubah menu")
    print("4. Kelola pegawai")
    print("5. Set metode pembayaran")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama menu: ")
        harga = int(input("Masukkan harga menu: "))
        menu.append({"nama": nama, "harga": harga})
        print("Menu berhasil ditambahkan.")
    elif pilihan == "2":
        for i, item in enumerate(menu):
            print(f"{i + 1}. {item['nama']} - Rp{item['harga']}")
        hapus = int(input("Pilih menu yang akan dihapus: ")) - 1
        if 0 <= hapus < len(menu):
            menu.pop(hapus)
            print("Menu berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    elif pilihan == "3":
        for i, item in enumerate(menu):
            print(f"{i + 1}. {item['nama']} - Rp{item['harga']}")
        ubah = int(input("Pilih menu yang akan diubah: ")) - 1
        if 0 <= ubah < len(menu):
            menu[ubah]["nama"] = input("Nama baru: ")
            menu[ubah]["harga"] = int(input("Harga baru: "))
            print("Menu berhasil diubah.")
        else:
            print("Pilihan tidak valid.")
    elif pilihan == "4":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        role = input("Masukkan role (admin/kasir): ")
        pegawai.append({"username": username, "password": password, "role": role})
        print("Pegawai berhasil ditambahkan.")
    elif pilihan == "5":
        metode_baru = input("Masukkan metode pembayaran baru: ")
        metode_pembayaran.append(metode_baru)
        print("Metode pembayaran berhasil ditambahkan.")
    else:
        print("Pilihan tidak valid.")


def menu_owner():
    print("\n=== Menu Owner ===")
    total_penjualan = sum([transaksi["total"] for transaksi in penjualan])
    print("Total Penjualan: Rp", total_penjualan)
    print("Laporan Grafik: (simulasi grafik)")


def login():
    print("\n=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in pegawai:
        if user["username"] == username and user["password"] == password:
            print(f"Login berhasil sebagai {user['role']}.")
            return user["role"]
    print("Username atau password salah.")
    return None


def main():
    while True:
        print("\n=== Sistem Manajemen Restoran ===")
        print("1. Pelanggan")
        print("2. Login (Pelayan/Kasir/Admin/Owner)")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_pelanggan()
        elif pilihan == "2":
            role = login()
            if role == "kasir":
                menu_kasir()
            elif role == "admin":
                menu_admin()
            elif role == "owner":
                menu_owner()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
