import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import json
import daftarmenu


# Variabel global
meja = None
pesanan = []
kritik_saran = None
total_harga = 0

def baca_menu():
    menu = {}

    # Coba membaca menu dari menu.json
    try:
        with open("menu.json", "r") as file:
            menu_json = json.load(file)
            if menu_json:
                menu.update(menu_json)
            else:
                update_status("Menu di file JSON kosong.", color="orange")
    except FileNotFoundError:
        update_status("File menu.json tidak ditemukan.", color="orange")
    except json.JSONDecodeError:
        update_status("Format menu.json tidak valid.", color="red")

    # Tambahkan menu dari daftarmenu.py
    menu.update({
        "Lalapan Ayam Goreng": daftarmenu.harga_lag,
        "Lalapan Jamur Crispy": daftarmenu.harga_ljc,
        "Lalapan Tempe Penyet": daftarmenu.harga_ltp,
        "Nasi Tempong Biasa": daftarmenu.harga_ntb,
        "Nasi Tempong Ayam": daftarmenu.harga_nta,
        "Nasi Goreng": daftarmenu.harga_ng,
        "Nasi Dadar Telur": daftarmenu.harga_ndt,
        "Ayam Geprek": daftarmenu.harga_ag,
        "Rujak Lontong": daftarmenu.harga_rl,
        "Rujak Kulup": daftarmenu.harga_rk,
        "Es Teh": daftarmenu.harga_et,
        "Es Lumut": daftarmenu.harga_el,
        "Cappucino Cincau": daftarmenu.harga_cc,
        "Es Buah": daftarmenu.harga_eb,
        "Air Mineral": daftarmenu.harga_am,
    })

    return menu



# Inisialisasi daftar menu dari file JSON
menu_harga = baca_menu()

# Fungsi untuk menyimpan data ke file JSON
def simpan_pesanan():
    if meja and pesanan:
        try:
            with open("pesanan.json", "r") as file:
                data_pesanan = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data_pesanan = {}

        data_pesanan[meja] = {
            "pesanan": pesanan,
            "total_harga": total_harga,
            "kritik_saran": kritik_saran or "Tidak ada"
        }

        with open("pesanan.json", "w") as file:
            json.dump(data_pesanan, file, indent=4)

        update_status("Pesanan berhasil disimpan!", color="green")
    else:
        update_status("Nomor meja atau pesanan kosong.", color="red")

# Fungsi untuk memperbarui status
class StatusDisplay:
    def __init__(self, ax):
        self.ax = ax
        self.texts = []

    def clear(self):
        for text in self.texts:
            text.remove()
        self.texts = []
        plt.draw()

    def append_text(self, message, fontsize=12, color="black"):
        y = 0.9 - len(self.texts) * 0.1
        text = self.ax.text(0.5, y, message, fontsize=fontsize, ha='center', va='center', color=color, transform=self.ax.transAxes)
        self.texts.append(text)
        plt.draw()

def update_status(message, color="black"):
    status_display.clear()
    status_display.append_text(message, fontsize=12, color=color)

# Fungsi untuk mengatur nomor meja
def set_meja(event):
    global meja
    meja = meja_box.text.strip()
    if meja:
        update_status(f"Meja {meja} disimpan!", color="green")
    else:
        update_status("Nomor meja tidak boleh kosong.", color="red")

def tambah_pesanan(event):
    global pesanan, total_harga
    item = pesanan_box.text.strip()
    if item:
        if item in menu_harga:
            pesanan.append(item)
            total_harga += menu_harga[item]
            update_status(f"Pesanan '{item}' ditambahkan! Total: Rp {total_harga:,}", color="blue")
        else:
            update_status(f"Menu '{item}' tidak ditemukan. Cek daftar: {list(menu_harga.keys())}", color="red")
    else:
        update_status("Pesanan tidak boleh kosong.", color="red")


# Fungsi untuk menyimpan kritik/saran
def simpan_kritik_saran(event):
    global kritik_saran
    kritik_saran = kritik_box.text.strip()
    update_status("Kritik dan saran disimpan.", color="green")

# Fungsi untuk checkout
def checkout(event):
    simpan_pesanan()

# Membuat antarmuka matplotlib
fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_visible(False)
ax.axis('off')

# Input untuk nomor meja
meja_box_ax = plt.axes([0.3, 0.85, 0.4, 0.05])
meja_box = TextBox(meja_box_ax, 'Nomor Meja: ', initial='')
meja_button_ax = plt.axes([0.75, 0.85, 0.15, 0.05])
meja_button = Button(meja_button_ax, 'Set Meja')
meja_button.on_clicked(set_meja)

# Input untuk pesanan
pesanan_box_ax = plt.axes([0.3, 0.75, 0.4, 0.05])
pesanan_box = TextBox(pesanan_box_ax, 'Pesanan: ', initial='')
pesanan_button_ax = plt.axes([0.75, 0.75, 0.15, 0.05])
pesanan_button = Button(pesanan_button_ax, 'Tambah Pesanan')
pesanan_button.on_clicked(tambah_pesanan)

# Input untuk kritik/saran
kritik_box_ax = plt.axes([0.3, 0.65, 0.4, 0.05])
kritik_box = TextBox(kritik_box_ax, 'Kritik/Saran: ', initial='')
kritik_button_ax = plt.axes([0.75, 0.65, 0.15, 0.05])
kritik_button = Button(kritik_button_ax, 'Simpan Saran')
kritik_button.on_clicked(simpan_kritik_saran)

# Tombol checkout
checkout_button_ax = plt.axes([0.3, 0.55, 0.4, 0.05])
checkout_button = Button(checkout_button_ax, 'Checkout')
checkout_button.on_clicked(checkout)

# Area status untuk pesan
status_display_ax = plt.axes([0.1, 0.1, 0.8, 0.4])
status_display_ax.axis('off')
status_display = StatusDisplay(status_display_ax)

plt.show()
