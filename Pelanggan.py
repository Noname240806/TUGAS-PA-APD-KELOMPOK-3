from prettytable import PrettyTable
from Data import kumpulan_bunga, data_pelanggan, total_transaksi_hari_ini, jumlah_pengunjung, diskon_member
from Promo import tampilkan_promo_hari_ini, cek_input_angka, hitung_diskon

def register_pelanggan():
    print("\n=== Registrasi Pelanggan Baru ===")
    nama = input("Masukkan nama: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter...")
        return
    if nama in data_pelanggan:
        print("Nama sudah terdaftar, silakan login.")
        input("Tekan Enter...")
        return
    pw = input("Masukkan password: ").strip()
    if not pw:
        print("Password wajib diisi!")
        input("Tekan Enter...")
        return
    data_pelanggan[nama] = pw
    print(f"Akun '{nama}' berhasil dibuat!")
    input("Tekan Enter...")

def dashboard_pelanggan(nama_pelanggan):
    global jumlah_pengunjung, total_transaksi_hari_ini
    jumlah_pengunjung += 1
    while True:
        print(f"""
        ==================================================
        [        TOKO BUNGA HIAS 💐 - PELANGGAN         ]
        ==================================================
        [1] Lihat Menu Bunga
        [2] Beli Bunga
        [3] Lihat Promo
        [0] Keluar
        ==================================================
        """)
        pilih = input("Pilih menu (0-3): ").strip()

        if pilih == "1":
            table = PrettyTable(["No", "Nama Bunga", "Harga", "Stok", "Warna"])
            for i, (nama, data) in enumerate(kumpulan_bunga.items(), 1):
                if data['stok'] > 0:
                    table.add_row([i, nama, f"Rp {data['harga']:,}", data['stok'], data['warna']])
            print(table)
            input("Tekan Enter...")

        elif pilih == "2":
            daftar_tersedia = [(n, d) for n, d in kumpulan_bunga.items() if d["stok"] > 0]
            if not daftar_tersedia:
                print("Maaf, semua bunga habis.")
                input("Tekan Enter...")
                continue
            for i, (nama, data) in enumerate(daftar_tersedia, 1):
                print(f"{i}. {nama} - Rp {data['harga']:,} (Stok: {data['stok']})")
            pilih_idx = input("\nPilih nomor bunga: ")
            if not pilih_idx.isdigit() or not (1 <= int(pilih_idx) <= len(daftar_tersedia)):
                print("Pilihan tidak valid!")
                input("Tekan Enter...")
                continue
            nama_beli, data_bunga = daftar_tersedia[int(pilih_idx) - 1]
            jumlah = cek_input_angka(f"Jumlah '{nama_beli}' yang dibeli: ")
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                input("Tekan Enter...")
                continue
            if jumlah > data_bunga["stok"]:
                print(f"Maaf, stok hanya {data_bunga['stok']}")
                input("Tekan Enter...")
                continue

            subtotal = data_bunga["harga"] * jumlah
            diskon = hitung_diskon(subtotal, diskon_member)
            total_bayar = subtotal - diskon

            kumpulan_bunga[nama_beli]["stok"] -= jumlah
            total_transaksi_hari_ini += total_bayar

            print(f"\nPembelian Berhasil!")
            print(f"Nama Bunga : {nama_beli}")
            print(f"Jumlah     : {jumlah}")
            print(f"Subtotal   : Rp {subtotal:,}")
            if diskon > 0:
                print(f"Diskon     : Rp {diskon:,}")
            print(f"Total Bayar: Rp {total_bayar:,}")
            print("\nTerima kasih telah berbelanja 🌸")
            input("\nTekan Enter...")

        elif pilih == "3":
            tampilkan_promo_hari_ini()
            input("Tekan Enter...")

        elif pilih == "0":
            print("Terima kasih telah berkunjung!")
            break
