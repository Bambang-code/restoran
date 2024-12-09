import json
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os

# Fungsi untuk membaca pesanan dari file
def baca_pesanan(file_path):
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return None

# Fungsi untuk memperbarui tampilan daftar pesanan
def perbarui_tampilan(event=None):
    data = baca_pesanan("pesanan.json")
    ax_pesanan.clear()
    ax_pesanan.axis('off')  # Pastikan axis tidak terlihat
    if data:
        ax_pesanan.text(0.5, 0.9, f"Meja: {data['meja']}", ha="center", va="center", fontsize=12, color="black")
        ax_pesanan.text(0.5, 0.8, "Pesanan:", ha="center", va="center", fontsize=12, color="black")
        for i, item in enumerate(data['pesanan'], start=1):
            ax_pesanan.text(0.1, 0.7 - i * 0.1, f"{i}. {item}", fontsize=10, color="blue", transform=ax_pesanan.transAxes)
        kritik_saran = data.get('kritik_saran', 'Tidak ada')
        total_harga = data.get('total_harga', 0)
        ax_pesanan.text(0.5, 0.2, f"Total Harga: Rp {total_harga:,}", ha="center", va="center", fontsize=12, color="orange")
        ax_pesanan.text(0.5, 0.1, f"Kritik dan Saran: {kritik_saran}", ha="center", va="center", fontsize=10, color="green")
    else:
        ax_pesanan.text(0.5, 0.5, "Belum ada pesanan.", ha="center", va="center", fontsize=12, color="red")
    plt.draw()

# Fungsi untuk keluar dari aplikasi
def keluar(event):
    plt.close()

# Membuat antarmuka matplotlib
fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_visible(False)  # Hapus latar belakang default
ax.axis('off')  # Hilangkan axis utama

# Area untuk menampilkan pesanan
ax_pesanan = plt.axes([0.1, 0.3, 0.8, 0.6])
ax_pesanan.axis('off')  # Hilangkan axis untuk area pesanan

# Tombol untuk memperbarui tampilan
refresh_button_ax = plt.axes([0.3, 0.15, 0.4, 0.05])
refresh_button = Button(refresh_button_ax, "Perbarui")
refresh_button.on_clicked(perbarui_tampilan)

# Tombol untuk keluar
exit_button_ax = plt.axes([0.3, 0.05, 0.4, 0.05])
exit_button = Button(exit_button_ax, "Keluar")
exit_button.on_clicked(keluar)

# Tampilkan antarmuka awal
perbarui_tampilan()
plt.show()
