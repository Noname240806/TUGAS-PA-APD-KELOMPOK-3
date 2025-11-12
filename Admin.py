from prettytable import PrettyTable
from Data import kumpulan_bunga, data_admin, total_transaksi_hari_ini, jumlah_pengunjung
from Promo import cek_input_angka

def register_admin():
    print("\n=== Daftarkan Admin Baru ===")
    nama = input("Nama admin baru: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan Enter...")
        return
    if nama in data_admin:
        print("Nama admin sudah digunakan!")
        input("Tekan Enter...")
        return
    password = input("Password: ").strip()
    if not password:
        print("Password wajib diisi!")
        input("Tekan Enter...")
        return
    data_admin[nama] = password
    print(f"Admin '{nama}' berhasil didaftarkan!")
    input("Tekan Enter...")

def dashboard_admin(nama_admin):
    global total_transaksi_hari_ini, jumlah_pengunjung
    while True:
        print(f"""
        ==================================================
        [           TOKO BUNGA HIAS 💐- ADMIN           ]
        ==================================================
        [1] Tambah Bunga Baru
        [2] Lihat Semua Bunga
        [3] Edit Bunga
        [4] Hapus Bunga
        [5] Daftarkan Admin Baru
        [6] Info Toko
        [0] Logout
        ==================================================
        """)
        pilih = input("Pilih menu (0-6): ").strip()

        if pilih == "1":
            print("=== Tambah Bunga Baru ===")
            nama = input("Nama bunga: ").strip()
            if not nama:
                print("Nama bunga tidak boleh kosong!")
                input("Tekan Enter...")
                continue
            harga = cek_input_angka("Harga (Rp): ")
            stok = cek_input_angka("Stok: ")
            warna = input("Warna: ").strip() or "Tidak disebutkan"
            kumpulan_bunga[nama] = {"harga": harga, "stok": stok, "warna": warna}
            print(f"Bunga '{nama}' berhasil ditambahkan!")
            input("Tekan Enter...")

        elif pilih == "2":
            print("\n=== Daftar Bunga ===")
            table = PrettyTable(["No", "Nama Bunga", "Harga", "Stok", "Warna"])
            for i, (nama, data) in enumerate(kumpulan_bunga.items(), 1):
                table.add_row([i, nama, f"Rp {data['harga']:,}", data['stok'], data['warna']])
            print(table)
            input("Tekan Enter...")

        elif pilih == "3":
            print("=== Edit Bunga ===")
            daftar = list(kumpulan_bunga.keys())
            for i, nama in enumerate(daftar, 1):
                print(f"{i}. {nama}")
            pilih_idx = input("\nPilih nomor bunga: ")
            if not pilih_idx.isdigit() or not (1 <= int(pilih_idx) <= len(daftar)):
                print("Pilihan tidak valid!")
                input("Tekan Enter...")
                continue
            nama_lama = daftar[int(pilih_idx) - 1]
            data = kumpulan_bunga[nama_lama]
            nama_baru = input(f"Nama baru [{nama_lama}]: ").strip() or nama_lama
            harga_baru = input(f"Harga baru [Rp {data['harga']:,}]: ").strip()
            stok_baru = input(f"Stok baru [{data['stok']}]: ").strip()
            warna_baru = input(f"Warna baru [{data['warna']}]: ").strip() or data["warna"]

            if nama_baru != nama_lama:
                kumpulan_bunga[nama_baru] = kumpulan_bunga.pop(nama_lama)
                data = kumpulan_bunga[nama_baru]

            if harga_baru.isdigit():
                data["harga"] = int(harga_baru)
            if stok_baru.isdigit():
                data["stok"] = int(stok_baru)
            data["warna"] = warna_baru

            print("Data bunga berhasil diperbarui!")
            input("Tekan Enter...")

        elif pilih == "4":
            print("=== Hapus Bunga ===")
            daftar = list(kumpulan_bunga.keys())
            for i, nama in enumerate(daftar, 1):
                print(f"{i}. {nama}")
            pilih_idx = input("\nPilih nomor bunga: ")
            if not pilih_idx.isdigit() or not (1 <= int(pilih_idx) <= len(daftar)):
                print("Pilihan tidak valid!")
                input("Tekan Enter...")
                continue
            nama_hapus = daftar[int(pilih_idx) - 1]
            konfirm = input(f"Yakin hapus '{nama_hapus}'? (y/n): ").lower()
            if konfirm == "y":
                del kumpulan_bunga[nama_hapus]
                print(f"Bunga '{nama_hapus}' dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            input("Tekan Enter...")

        elif pilih == "5":
            register_admin()

        elif pilih == "6":
            print("=== INFO TOKO BUNGA HIAS ===")
            print(f"Jumlah admin: {len(data_admin)}")
            print(f"Pengunjung hari ini: {jumlah_pengunjung}")
            total_stok_nilai = sum(b["harga"] * b["stok"] for b in kumpulan_bunga.values())
            print(f"Total nilai stok: Rp {total_stok_nilai:,}")
            print(f"Total transaksi hari ini: Rp {total_transaksi_hari_ini:,}")
            input("\nTekan Enter...")

        elif pilih == "0":
            print("Anda telah logout.")
            input("Tekan Enter...")
            break
