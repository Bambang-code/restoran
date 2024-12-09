import json
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import os

# Variabel global
total_penjualan = 0

# Fungsi untuk membaca pesanan dari file JSON
def baca_pesanan(file_path):
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return None

# Fungsi untuk membaca daftar menu dari file JSON
def baca_menu():
    try:
        with open("menu.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Fungsi untuk memperbarui tampilan daftar pesanan
def perbarui_tampilan(event=None):
    global total_penjualan
    menu_harga = baca_menu()  # Baca data menu terbaru
    data = baca_pesanan("pesanan.json")
    ax_pesanan.clear()
    ax_pesanan.axis('off')
    if data:
        total_bayar = data.get("total_harga", 0)
        total_penjualan += total_bayar

        # Tampilkan detail pesanan
        ax_pesanan.text(0.5, 0.9, f"Meja: {data['meja']}", ha="center", va="center", fontsize=12, color="black")
        ax_pesanan.text(0.5, 0.8, "Pesanan:", ha="center", va="center", fontsize=12, color="black")
        for i, item in enumerate(data['pesanan'], start=1):
            harga = menu_harga.get(item, 0)
            ax_pesanan.text(
                0.1, 0.7 - i * 0.1, f"{i}. {item} - Rp {harga:,}", fontsize=10, color="blue", transform=ax_pesanan.transAxes
            )
        ax_pesanan.text(0.5, 0.2, f"Total Bayar: Rp {total_bayar:,}", ha="center", va="center", fontsize=12, color="orange")
    else:
        ax_pesanan.text(0.5, 0.5, "Tidak ada pesanan yang ditemukan.", ha="center", va="center", fontsize=12, color="red")
    plt.draw()

# Fungsi untuk menampilkan total penjualan
def tampilkan_total_penjualan(event):
    ax_total_penjualan.clear()
    ax_total_penjualan.axis('off')
    ax_total_penjualan.text(
        0.5, 0.5, f"Total Penjualan: Rp {total_penjualan:,}", ha="center", va="center", fontsize=12, color="green"
    )
    plt.draw()

# Fungsi untuk memilih metode pembayaran
def pilih_metode_bayar(event):
    metode = metode_box.text.strip()
    ax_metode_bayar.clear()
    ax_metode_bayar.axis('off')
    if metode in ["Tunai", "Kartu", "QRIS"]:
        ax_metode_bayar.text(
            0.5, 0.5, f"Metode Pembayaran: {metode}", ha="center", va="center", fontsize=12, color="blue"
        )
    else:
        ax_metode_bayar.text(
            0.5, 0.5, "Metode pembayaran tidak valid!", ha="center", va="center", fontsize=12, color="red"
        )
    plt.draw()

# Fungsi untuk keluar dari aplikasi
def keluar(event):
    plt.close()

# Membuat antarmuka matplotlib
fig, ax = plt.subplots(figsize=(8, 10))
fig.patch.set_visible(False)
ax.axis('off')

# Area untuk menampilkan pesanan
ax_pesanan = plt.axes([0.1, 0.6, 0.8, 0.3])
ax_pesanan.axis('off')

# Area untuk menampilkan total penjualan
ax_total_penjualan = plt.axes([0.1, 0.4, 0.8, 0.1])
ax_total_penjualan.axis('off')

# Input untuk metode pembayaran
metode_box_ax = plt.axes([0.3, 0.3, 0.4, 0.05])
metode_box = TextBox(metode_box_ax, 'Metode Bayar (Tunai/Kartu/QRIS): ', initial='')
metode_button_ax = plt.axes([0.75, 0.3, 0.15, 0.05])
metode_button = Button(metode_button_ax, 'Pilih')
metode_button.on_clicked(pilih_metode_bayar)

# Area untuk menampilkan metode pembayaran
ax_metode_bayar = plt.axes([0.1, 0.2, 0.8, 0.05])
ax_metode_bayar.axis('off')

# Tombol untuk memperbarui daftar pesanan
refresh_button_ax = plt.axes([0.1, 0.1, 0.3, 0.05])
refresh_button = Button(refresh_button_ax, 'Perbarui Pesanan')
refresh_button.on_clicked(perbarui_tampilan)

# Tombol untuk menampilkan total penjualan
total_button_ax = plt.axes([0.5, 0.1, 0.3, 0.05])
total_button = Button(total_button_ax, 'Total Penjualan')
total_button.on_clicked(tampilkan_total_penjualan)

# Tombol untuk keluar
exit_button_ax = plt.axes([0.85, 0.1, 0.1, 0.05])
exit_button = Button(exit_button_ax, 'Keluar')
exit_button.on_clicked(keluar)

# Tampilkan antarmuka awal
perbarui_tampilan()
plt.show()
