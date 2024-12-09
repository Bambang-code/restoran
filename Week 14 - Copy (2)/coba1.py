import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.image as mpimg

# Inisialisasi counter dan harga
counter_lag = 0
counter_ljc = 0
counter_ltp = 0
counter_ntb = 0
counter_nta = 0
counter_ng = 0
counter_ndt = 0
counter_ag = 0
counter_rl = 0
counter_rk = 0
counter_et = 0
counter_el = 0
counter_cc = 0
counter_eb = 0
counter_am = 0
harga_lag = 12000
harga_ljc = 10000
harga_ltp = 10000
harga_ntb = 10000
harga_nta = 12000
harga_ng = 8000
harga_ndt = 10000
harga_ag = 10000
harga_rl = 9000
harga_rk = 9000
harga_et = 3000
harga_el = 3000
harga_cc = 3000
harga_eb = 4000
harga_am = 2500
fig = plt.figure()
fig.suptitle('Toko Mracangan', fontsize=14, fontweight='bold')

# Fungsi untuk menangani klik tombol Sabun
def on_button_click_lag(event):
    global counter_lag
    counter_lag += 1
    update_counter_text()

# Fungsi untuk menangani klik tombol Pewangi
def on_button_click_ljc(event):
    global counter_ljc
    counter_ljc += 1
    update_counter_text()
    
def on_button_click_ltp(event):
    global counter_ltp
    counter_ltp += 1
    update_counter_text()
    
def on_button_click_ntb(event):
    global counter_ntb
    counter_ntb += 1
    update_counter_text()
    
def on_button_click_nta(event):
    global counter_nta
    counter_nta += 1
    update_counter_text()
    
def on_button_click_ng(event):
    global counter_ng
    counter_ng += 1
    update_counter_text()
    
def on_button_click_ndt(event):
    global counter_ndt
    counter_ndt += 1
    update_counter_text()
    
def on_button_click_ag(event):
    global counter_ag
    counter_ag += 1
    update_counter_text()
    
def on_button_click_rl(event):
    global counter_rl
    counter_rl += 1
    update_counter_text()
    
def on_button_click_rk(event):
    global counter_rk
    counter_rk += 1
    update_counter_text()
    
def on_button_click_et(event):
    global counter_et
    counter_et += 1
    update_counter_text()
    
def on_button_click_el(event):
    global counter_el
    counter_el += 1
    update_counter_text()
    
def on_button_click_cc(event):
    global counter_cc
    counter_cc += 1
    update_counter_text()
    
def on_button_click_eb(event):
    global counter_eb
    counter_eb += 1
    update_counter_text()
    
def on_button_click_am(event):
    global counter_am
    counter_am += 1
    update_counter_text()

# Fungsi untuk memperbarui teks counter dan subtotal
def update_counter_text():
    ax_counter_lag.clear()
    ax_counter_ljc.clear()
    ax_counter_ltp.clear()
    ax_counter_ntb.clear()
    ax_counter_nta.clear()
    ax_counter_ng.clear()
    ax_counter_ndt.clear()
    ax_counter_ag.clear()
    ax_counter_rl.clear()
    ax_counter_rk.clear()
    ax_counter_et.clear()
    ax_counter_el.clear()
    ax_counter_cc.clear()
    ax_counter_eb.clear()
    ax_counter_am.clear()
    ax_total_lag.clear()
    ax_total_ljc.clear()
    ax_total_ltp.clear()
    ax_total_ntb.clear()
    ax_total_nta.clear()
    ax_total_ng.clear()
    ax_total_ndt.clear()
    ax_total_ag.clear()
    ax_total_rl.clear()
    ax_total_rk.clear()
    ax_total_et.clear()
    ax_total_el.clear()
    ax_total_cc.clear()
    ax_total_eb.clear()
    ax_total_am.clear()
    ax_subtotal.clear()
    
    # Perbarui jumlah untuk Sabun dan Pewangi
    ax_counter_lag.text(0.5, 0.5, f"{counter_lag} x Rp {harga_lag:,}", fontsize=10, ha='center', va='center')
    ax_counter_ljc.text(0.5, 0.5, f"{counter_ljc} x Rp {harga_ljc:,}", fontsize=10, ha='center', va='center')
    ax_counter_ltp.text(0.5, 0.5, f"{counter_ltp} x Rp {harga_ltp:,}", fontsize=10, ha='center', va='center')
    ax_counter_ntb.text(0.5, 0.5, f"{counter_ntb} x Rp {harga_ntb:,}", fontsize=10, ha='center', va='center')
    ax_counter_nta.text(0.5, 0.5, f"{counter_nta} x Rp {harga_nta:,}", fontsize=10, ha='center', va='center')
    ax_counter_ng.text(0.5, 0.5, f"{counter_ng} x Rp {harga_ng:,}", fontsize=10, ha='center', va='center')
    ax_counter_ndt.text(0.5, 0.5, f"{counter_ndt} x Rp {harga_ndt:,}", fontsize=10, ha='center', va='center')
    ax_counter_ag.text(0.5, 0.5, f"{counter_ag} x Rp {harga_ag:,}", fontsize=10, ha='center', va='center')
    ax_counter_rl.text(0.5, 0.5, f"{counter_rl} x Rp {harga_rl:,}", fontsize=10, ha='center', va='center')
    ax_counter_rk.text(0.5, 0.5, f"{counter_rk} x Rp {harga_rk:,}", fontsize=10, ha='center', va='center')
    ax_counter_et.text(0.5, 0.5, f"{counter_et} x Rp {harga_et:,}", fontsize=10, ha='center', va='center')
    ax_counter_el.text(0.5, 0.5, f"{counter_el} x Rp {harga_el:,}", fontsize=10, ha='center', va='center')
    ax_counter_cc.text(0.5, 0.5, f"{counter_cc} x Rp {harga_cc:,}", fontsize=10, ha='center', va='center')
    ax_counter_eb.text(0.5, 0.5, f"{counter_eb} x Rp {harga_eb:,}", fontsize=10, ha='center', va='center')
    ax_counter_am.text(0.5, 0.5, f"{counter_am} x Rp {harga_am:,}", fontsize=10, ha='center', va='center')
    
    # Perbarui total harga untuk Sabun dan Pewangi
    total_lag = counter_lag * harga_lag
    total_ljc = counter_ljc * harga_ljc
    total_ltp = counter_ltp * harga_ltp
    total_ntb = counter_ntb * harga_ntb
    total_nta = counter_nta * harga_nta
    total_ng = counter_ng * harga_ng
    total_ndt = counter_ndt * harga_ndt
    total_ag = counter_ag * harga_ag
    total_rl = counter_rl * harga_rl
    total_rk = counter_rk * harga_rk
    total_et = counter_et * harga_et
    total_el = counter_el * harga_el
    total_cc = counter_cc * harga_cc
    total_eb = counter_eb * harga_eb
    total_am = counter_am * harga_am
    ax_total_lag.text(0.5, 0.5, f"Rp {total_lag:,}", fontsize=12, ha='center', va='center')
    ax_total_ljc.text(0.5, 0.5, f"Rp {total_ljc:,}", fontsize=12, ha='center', va='center')
    ax_total_ltp.text(0.5, 0.5, f"Rp {total_ltp:,}", fontsize=12, ha='center', va='center')
    ax_total_ntb.text(0.5, 0.5, f"Rp {total_ntb:,}", fontsize=12, ha='center', va='center')
    ax_total_nta.text(0.5, 0.5, f"Rp {total_nta:,}", fontsize=12, ha='center', va='center')
    ax_total_ng.text(0.5, 0.5, f"Rp {total_ng:,}", fontsize=12, ha='center', va='center')
    ax_total_ndt.text(0.5, 0.5, f"Rp {total_ndt:,}", fontsize=12, ha='center', va='center')
    ax_total_ag.text(0.5, 0.5, f"Rp {total_ag:,}", fontsize=12, ha='center', va='center')
    ax_total_rl.text(0.5, 0.5, f"Rp {total_rl:,}", fontsize=12, ha='center', va='center')
    ax_total_rk.text(0.5, 0.5, f"Rp {total_rk:,}", fontsize=12, ha='center', va='center')
    ax_total_et.text(0.5, 0.5, f"Rp {total_et:,}", fontsize=12, ha='center', va='center')
    ax_total_el.text(0.5, 0.5, f"Rp {total_el:,}", fontsize=12, ha='center', va='center')
    ax_total_cc.text(0.5, 0.5, f"Rp {total_cc:,}", fontsize=12, ha='center', va='center')
    ax_total_eb.text(0.5, 0.5, f"Rp {total_eb:,}", fontsize=12, ha='center', va='center')
    ax_total_am.text(0.5, 0.5, f"Rp {total_am:,}", fontsize=12, ha='center', va='center')
    
    # Perbarui subtotal keseluruhan
    subtotal = total_lag + total_ljc + total_ltp + total_ntb + total_nta + total_ng + total_ndt + total_ag + total_rl + total_rk + total_et + total_el + total_cc + total_eb + total_am
    ax_subtotal.text(0.5, 0.5, f"Total: Rp {subtotal:,}", fontsize=14, ha='center', va='center', fontweight='bold')
    
    ax_counter_lag.axis('off')
    ax_counter_ljc.axis('off')
    ax_counter_ltp.axis('off')
    ax_counter_ntb.axis('off')
    ax_counter_nta.axis('off')
    ax_counter_ng.axis('off')
    ax_counter_ndt.axis('off')
    ax_counter_ag.axis('off')
    ax_counter_rl.axis('off')
    ax_counter_rk.axis('off')
    ax_counter_et.axis('off')
    ax_counter_el.axis('off')
    ax_counter_cc.axis('off')
    ax_counter_eb.axis('off')
    ax_counter_am.axis('off')
    ax_total_lag.axis('off')
    ax_total_ljc.axis('off')
    ax_total_ltp.axis('off')
    ax_total_ntb.axis('off')
    ax_total_nta.axis('off')
    ax_total_ng.axis('off')
    ax_total_ndt.axis('off')
    ax_total_ag.axis('off')
    ax_total_rl.axis('off')
    ax_total_rk.axis('off')
    ax_total_et.axis('off')
    ax_total_el.axis('off')
    ax_total_cc.axis('off')
    ax_total_eb.axis('off')
    ax_total_am.axis('off')
    ax_subtotal.axis('off')

    plt.draw()

# Menyiapkan tombol Sabun
axButn1 = plt.axes([0.01, 0.3, 0.1, 0.1]) 
btn1 = Button(axButn1, label="", color='pink', hovercolor='tomato')
img_lag = mpimg.imread('lag.jpg')  
axButn1.imshow(img_lag)
axButn1.axis('off')  # Menyembunyikan axis
btn1.on_clicked(on_button_click_lag)
axButn1.text(0.5, 1.1, 'Lalapan Ayam Goreng', ha='center', va='bottom', transform=axButn1.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

# Menyiapkan tombol Pewangi
axButn2 = plt.axes([0.2, 0.3, 0.1, 0.1]) 
btn2 = Button(axButn2, label="", color='lightblue', hovercolor='deepskyblue')
img_ljc = mpimg.imread('ljc.jpg')  
axButn2.imshow(img_ljc)
axButn2.axis('off')  # Menyembunyikan axis
btn2.on_clicked(on_button_click_ljc)
axButn2.text(0.5, 1.1, 'Lalapan Jamur Crispy', ha='center', va='bottom', transform=axButn2.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar


axButn3 = plt.axes([0.4, 0.3, 0.1, 0.1]) 
btn3 = Button(axButn3, label="", color='lightblue', hovercolor='deepskyblue')
img_ltp = mpimg.imread('ltp.jpg')  
axButn3.imshow(img_ltp)
axButn3.axis('off')  # Menyembunyikan axis
btn3.on_clicked(on_button_click_ltp)
axButn3.text(0.5, 1.1, 'Lalapan Tempe Penyet', ha='center', va='bottom', transform=axButn3.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn4 = plt.axes([0.6, 0.3, 0.1, 0.1]) 
btn4 = Button(axButn4, label="", color='lightblue', hovercolor='deepskyblue')
img_ntb = mpimg.imread('ntb.jpg')  
axButn4.imshow(img_ntb)
axButn4.axis('off')  # Menyembunyikan axis
btn4.on_clicked(on_button_click_ntb)
axButn4.text(0.5, 1.1, 'Nasi Tempong Biasa', ha='center', va='bottom', transform=axButn4.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn5 = plt.axes([0.8, 0.3, 0.1, 0.1]) 
btn5 = Button(axButn5, label="", color='lightblue', hovercolor='deepskyblue')
img_nta = mpimg.imread('nta.jpg')  
axButn5.imshow(img_nta)
axButn5.axis('off')  # Menyembunyikan axis
btn5.on_clicked(on_button_click_nta)
axButn5.text(0.5, 1.1, 'Nasi Tempong Ayam', ha='center', va='bottom', transform=axButn5.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn6 = plt.axes([0.01, 0.5, 0.1, 0.1]) 
btn6 = Button(axButn6, label="", color='lightblue', hovercolor='deepskyblue')
img_ng = mpimg.imread('ng.jpg')  
axButn6.imshow(img_ng)
axButn6.axis('off')  # Menyembunyikan axis
btn6.on_clicked(on_button_click_ng)
axButn6.text(0.5, 1.1, 'Nasi Goreng', ha='center', va='bottom', transform=axButn6.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn7 = plt.axes([0.2, 0.5, 0.1, 0.1]) 
btn7 = Button(axButn7, label="", color='lightblue', hovercolor='deepskyblue')
img_ndt = mpimg.imread('ndt.jpg')  
axButn7.imshow(img_ndt)
axButn7.axis('off')  # Menyembunyikan axis
btn7.on_clicked(on_button_click_ndt)
axButn7.text(0.5, 1.1, 'Nasi Dadar Telur', ha='center', va='bottom', transform=axButn7.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn8 = plt.axes([0.4, 0.5, 0.1, 0.1]) 
btn8 = Button(axButn8, label="", color='lightblue', hovercolor='deepskyblue')
img_ag = mpimg.imread('ag.jpeg')  
axButn8.imshow(img_ag)
axButn8.axis('off')  # Menyembunyikan axis
btn8.on_clicked(on_button_click_ag)
axButn8.text(0.5, 1.1, 'Ayam Geprek', ha='center', va='bottom', transform=axButn8.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn9 = plt.axes([0.6, 0.5, 0.1, 0.1]) 
btn9 = Button(axButn9, label="", color='lightblue', hovercolor='deepskyblue')
img_rl = mpimg.imread('rl.jpg')  
axButn9.imshow(img_rl)
axButn9.axis('off')  # Menyembunyikan axis
btn9.on_clicked(on_button_click_rl)
axButn9.text(0.5, 1.1, 'Rujak Lontong', ha='center', va='bottom', transform=axButn9.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn10 = plt.axes([0.8, 0.5, 0.1, 0.1]) 
btn10 = Button(axButn10, label="", color='lightblue', hovercolor='deepskyblue')
img_rk = mpimg.imread('rk.jpg')  
axButn10.imshow(img_rk)
axButn10.axis('off')  # Menyembunyikan axis
btn10.on_clicked(on_button_click_rk)
axButn10.text(0.5, 1.1, 'Rujak Kulup', ha='center', va='bottom', transform=axButn10.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn11 = plt.axes([0.01, 0.7, 0.1, 0.1]) 
btn11 = Button(axButn11, label="", color='lightblue', hovercolor='deepskyblue')
img_et = mpimg.imread('et.jpeg')  
axButn11.imshow(img_et)
axButn11.axis('off')  # Menyembunyikan axis
btn11.on_clicked(on_button_click_et)
axButn11.text(0.5, 1.1, 'Es Teh', ha='center', va='bottom', transform=axButn11.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn12= plt.axes([0.2, 0.7, 0.1, 0.1]) 
btn12 = Button(axButn12, label="", color='lightblue', hovercolor='deepskyblue')
img_el = mpimg.imread('el.jpeg')  
axButn12.imshow(img_el)
axButn12.axis('off')  # Menyembunyikan axis
btn12.on_clicked(on_button_click_el)
axButn12.text(0.5, 1.1, 'Es Lumut', ha='center', va='bottom', transform=axButn12.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn13 = plt.axes([0.4, 0.7, 0.1, 0.1]) 
btn13 = Button(axButn13, label="", color='lightblue', hovercolor='deepskyblue')
img_cc = mpimg.imread('cc.jpeg')  
axButn13.imshow(img_cc)
axButn13.axis('off')  # Menyembunyikan axis
btn13.on_clicked(on_button_click_cc)
axButn13.text(0.5, 1.1, 'Cappucino Cincau', ha='center', va='bottom', transform=axButn13.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn14 = plt.axes([0.6, 0.7, 0.1, 0.1]) 
btn14 = Button(axButn14, label="", color='lightblue', hovercolor='deepskyblue')
img_eb = mpimg.imread('eb.jpeg')  
axButn14.imshow(img_eb)
axButn14.axis('off')  # Menyembunyikan axis
btn14.on_clicked(on_button_click_eb)
axButn14.text(0.5, 1.1, 'Es Buah', ha='center', va='bottom', transform=axButn14.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

axButn15 = plt.axes([0.8, 0.7, 0.1, 0.1]) 
btn15 = Button(axButn15, label="", color='lightblue', hovercolor='deepskyblue')
img_am = mpimg.imread('am.jpeg')  
axButn15.imshow(img_am)
axButn15.axis('off')  # Menyembunyikan axis
btn15.on_clicked(on_button_click_am)
axButn15.text(0.5, 1.1, 'Air Mineral', ha='center', va='bottom', transform=axButn15.transAxes, fontsize=5, fontweight='bold')  # Nama di atas gambar

# Menyiapkan axes untuk jumlah dan harga per item
ax_counter_lag = plt.axes([0.01, 0.42, 0.1, 0.05])  # Posisi untuk jumlah dan harga sabun
ax_counter_ljc = plt.axes([0.2, 0.42, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_ltp = plt.axes([0.4, 0.42, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_ntb = plt.axes([0.6, 0.42, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_nta = plt.axes([0.8, 0.42, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_ng = plt.axes([0.01, 0.62, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_ndt = plt.axes([0.2, 0.62, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_ag = plt.axes([0.4, 0.62, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_rl = plt.axes([0.6, 0.62, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_rk = plt.axes([0.8, 0.62, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_et = plt.axes([0.01, 0.82, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_el = plt.axes([0.2, 0.82, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_cc = plt.axes([0.4, 0.82, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_eb = plt.axes([0.6, 0.82, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi
ax_counter_am = plt.axes([0.8, 0.82, 0.1, 0.05])  # Posisi untuk jumlah dan harga pewangi

# Menyiapkan axes untuk total harga per item
ax_total_lag = plt.axes([0.01, 0.25, 0.1, 0.05])
ax_total_ljc = plt.axes([0.2, 0.25, 0.1, 0.05])
ax_total_ltp = plt.axes([0.4, 0.25, 0.1, 0.05])
ax_total_ntb = plt.axes([0.6, 0.25, 0.1, 0.05])
ax_total_nta = plt.axes([0.8, 0.25, 0.1, 0.05])
ax_total_ng = plt.axes([0.01, 0.45, 0.1, 0.05])
ax_total_ndt = plt.axes([0.2, 0.45, 0.1, 0.05])
ax_total_ag = plt.axes([0.4, 0.45, 0.1, 0.05])
ax_total_rl = plt.axes([0.6, 0.45, 0.1, 0.05])
ax_total_rk = plt.axes([0.8, 0.45, 0.1, 0.05])
ax_total_et = plt.axes([0.01, 0.65, 0.1, 0.05])
ax_total_el = plt.axes([0.2, 0.65, 0.1, 0.05])
ax_total_cc = plt.axes([0.4, 0.65, 0.1, 0.05])
ax_total_eb = plt.axes([0.6, 0.65, 0.1, 0.05])
ax_total_am = plt.axes([0.8, 0.65, 0.1, 0.05])
# Menyiapkan axes untuk subtotal keseluruhan di kanan bawah
ax_subtotal = plt.axes([0.7, 0.05, 0.2, 0.05])

# Memperbarui teks counter dan subtotal awal
update_counter_text()

# Menampilkan plot
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)
plt.show()

