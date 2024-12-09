import matplotlib.pyplot as plt

def tampilkan_bon(nomor_meja, pesanan, subtotal):
    fig, ax = plt.subplots(figsize=(6, 8))
    fig.suptitle(f"Bon - Meja {nomor_meja}", fontsize=16, fontweight='bold')

    ax.axis('off')  # Nonaktifkan axis

    # Header bon
    y_pos = 0.9
    ax.text(0.5, y_pos, "Toko Mracangan", fontsize=14, ha='center', va='center', transform=ax.transAxes)
    y_pos -= 0.1

    # Daftar pesanan
    for i, item in enumerate(pesanan, start=1):
        ax.text(0.1, y_pos, f"{i}. {item['nama']} x {item['jumlah']} = Rp {item['harga']:,}", 
                fontsize=12, ha='left', va='center', transform=ax.transAxes)
        y_pos -= 0.05

    # Subtotal
    y_pos -= 0.05
    ax.text(0.1, y_pos, f"Subtotal: Rp {subtotal:,}", fontsize=12, ha='left', va='center', transform=ax.transAxes, color="green")

    # Footer
    y_pos -= 0.1
    ax.text(0.5, y_pos, "Terima kasih atas kunjungan Anda!", fontsize=12, ha='center', va='center', transform=ax.transAxes, color="blue")

    plt.show()
