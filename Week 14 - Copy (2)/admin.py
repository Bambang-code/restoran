import json
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import pandas as pd

# File untuk menyimpan data
MENU_FILE = "menu.json"
PEGAWAI_FILE = "pegawai.json"
USER_CSV_FILE = "users_data_final.csv"  # File CSV untuk data pegawai

# Fungsi membaca data dari file JSON
def baca_data(file_path):
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

# Fungsi menulis data ke file JSON
def tulis_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Fungsi membaca data pegawai dari file CSV
def baca_pegawai_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return dict(zip(df["Username"], df["Password"]))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
        return {}

# Fungsi menulis data pegawai ke file CSV
def tulis_pegawai_csv(file_path, data):
    df = pd.DataFrame(list(data.items()), columns=["Username", "Password"])
    df.to_csv(file_path, index=False)

# Inisialisasi data
menu_data = baca_data(MENU_FILE)
pegawai_data = baca_pegawai_csv(USER_CSV_FILE)

# Fungsi untuk menampilkan pesan di antarmuka
def tampilkan_pesan(message, color="black"):
    ax_status.clear()
    ax_status.text(0.5, 0.5, message, ha='center', va='center', fontsize=12, color=color)
    plt.draw()

# Fungsi menambah menu
def tambah_menu(event):
    nama_menu = menu_name_box.text.strip()
    try:
        harga_menu = int(menu_price_box.text.strip())
        if nama_menu and harga_menu > 0:
            menu_data[nama_menu] = harga_menu
            tulis_data(MENU_FILE, menu_data)
            tampilkan_pesan(f"Menu '{nama_menu}' berhasil ditambahkan!", color="green")
        else:
            tampilkan_pesan("Nama menu atau harga tidak valid.", color="red")
    except ValueError:
        tampilkan_pesan("Harga harus berupa angka.", color="red")

# Fungsi menghapus menu
def hapus_menu(event):
    nama_menu = menu_name_box.text.strip()
    if nama_menu in menu_data:
        del menu_data[nama_menu]
        tulis_data(MENU_FILE, menu_data)
        tampilkan_pesan(f"Menu '{nama_menu}' berhasil dihapus!", color="green")
    else:
        tampilkan_pesan(f"Menu '{nama_menu}' tidak ditemukan.", color="red")

# Fungsi memperbarui harga menu
def update_harga_menu(event):
    nama_menu = menu_name_box.text.strip()
    try:
        harga_baru = int(menu_price_box.text.strip())
        if nama_menu in menu_data:
            menu_data[nama_menu] = harga_baru
            tulis_data(MENU_FILE, menu_data)
            tampilkan_pesan(f"Harga menu '{nama_menu}' berhasil diperbarui!", color="green")
        else:
            tampilkan_pesan(f"Menu '{nama_menu}' tidak ditemukan.", color="red")
    except ValueError:
        tampilkan_pesan("Harga harus berupa angka.", color="red")

# Fungsi menambah pegawai
def tambah_pegawai(event):
    username = pegawai_name_box.text.strip()
    password = pegawai_pass_box.text.strip()
    if username and password:
        pegawai_data[username] = password
        tulis_pegawai_csv(USER_CSV_FILE, pegawai_data)
        tampilkan_pesan(f"Pegawai '{username}' berhasil ditambahkan!", color="green")
    else:
        tampilkan_pesan("Username atau password tidak valid.", color="red")

# Fungsi mengubah password pegawai
def ubah_password_pegawai(event):
    username = pegawai_name_box.text.strip()
    password_baru = pegawai_pass_box.text.strip()
    if username in pegawai_data:
        if password_baru:
            pegawai_data[username] = password_baru
            tulis_pegawai_csv(USER_CSV_FILE, pegawai_data)
            tampilkan_pesan(f"Password untuk '{username}' berhasil diubah!", color="green")
        else:
            tampilkan_pesan("Password baru tidak boleh kosong.", color="red")
    else:
        tampilkan_pesan(f"Pegawai '{username}' tidak ditemukan.", color="red")

# Membuat antarmuka Matplotlib
fig, ax = plt.subplots(figsize=(8, 10))
fig.patch.set_visible(False)
ax.axis('off')

# Input untuk menu
ax_menu_name = plt.axes([0.1, 0.8, 0.3, 0.05])
menu_name_box = TextBox(ax_menu_name, "Nama Menu: ")
ax_menu_price = plt.axes([0.1, 0.7, 0.3, 0.05])
menu_price_box = TextBox(ax_menu_price, "Harga Menu: ")

# Tombol untuk menu
ax_add_menu = plt.axes([0.5, 0.8, 0.3, 0.05])
add_menu_button = Button(ax_add_menu, "Tambah Menu")
add_menu_button.on_clicked(tambah_menu)

ax_remove_menu = plt.axes([0.5, 0.7, 0.3, 0.05])
remove_menu_button = Button(ax_remove_menu, "Hapus Menu")
remove_menu_button.on_clicked(hapus_menu)

ax_update_menu = plt.axes([0.5, 0.6, 0.3, 0.05])
update_menu_button = Button(ax_update_menu, "Update Harga")
update_menu_button.on_clicked(update_harga_menu)

# Input untuk pegawai
ax_pegawai_name = plt.axes([0.1, 0.5, 0.3, 0.05])
pegawai_name_box = TextBox(ax_pegawai_name, "Username Pegawai: ")
ax_pegawai_pass = plt.axes([0.1, 0.4, 0.3, 0.05])
pegawai_pass_box = TextBox(ax_pegawai_pass, "Password Pegawai: ")

# Tombol untuk pegawai
ax_add_pegawai = plt.axes([0.5, 0.5, 0.3, 0.05])
add_pegawai_button = Button(ax_add_pegawai, "Tambah Pegawai")
add_pegawai_button.on_clicked(tambah_pegawai)

ax_update_password = plt.axes([0.5, 0.4, 0.3, 0.05])
update_password_button = Button(ax_update_password, "Ubah Password")
update_password_button.on_clicked(ubah_password_pegawai)

# Area untuk pesan status
ax_status = plt.axes([0.1, 0.1, 0.8, 0.1])
ax_status.axis('off')

# Menampilkan antarmuka
plt.show()
