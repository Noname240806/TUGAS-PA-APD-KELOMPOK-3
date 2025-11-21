from prettytable import PrettyTable
from Data import kumpulan_bunga, data_admin, total_transaksi_hari_ini, jumlah_pengunjung
from Promo import cek_input_angka

def register_admin():
    print("\n=== Daftarkan Admin Baru ===")
    nama = input("Nama Admin Baru: ").strip()
    if not nama:
        print("Nama Tidak Boleh Kosong!")
        input("Tekan Enter...")
        return
    if nama in data_admin:
        print("Nama Admin Sudah Digunakan! Silahkan Coba Nama Lain")
        input("Tekan Enter...")
        return
    password = input("Password: ").strip()
    if not password:
        print("Password Wajib Diisi!")
        input("Tekan Enter...")
        return
    data_admin[nama] = password
    print(f"Admin '{nama}' Berhasil Didaftarkan!")
    input("Tekan Enter...")

def dashboard_admin(nama_admin):
    global total_transaksi_hari_ini, jumlah_pengunjung
    while True:
        print(f"""
        ==================================================
        [           TOKO BUNGA HIAS💐- MENU ADMIN       ]
        ==================================================
        [1] Tambah Bunga Baru
        [2] Lihat Semua Bunga
        [3] Edit Bunga
        [4] Hapus Bunga
        [5] Daftarkan Admin Baru
        [6] Riwayat Pembelian Pelanggan
        [0] Logout
        ==================================================
        """)
        pilih = input("Pilih menu (0-6): ").strip()

        if pilih == "1":
            print("=== Tambah Bunga Baru ===")


            while True:
                nama = input("Nama Bunga: ").strip()
                if not nama:
                    print("Nama Bunga Tidak Boleh Kosong!")
                elif nama in kumpulan_bunga:
                    print("Nama Bunga Sudah Ada!")
                else:
                    break

            while True:
                harga = cek_input_angka("Harga (Rp): ")
                if harga <= 0:
                    print("Harga Harus Lebih Dari 0!")
                elif harga > 10_000_000:
                    print("Harga Terlalu Tinggi! Maksimal Rp 10.000.000")
                else:
                    break

            while True:
                stok = cek_input_angka("Stok: ")
                if stok <= 0:
                    print("Stok Harus Lebih Dari 0!")
                else:
                    break

            while True:
                warna = input("Warna: ").strip()
                if warna:
                    break
                print("Warna Tidak Boleh Kosong!")

            kumpulan_bunga[nama] = {"harga": harga, "stok": stok, "warna": warna}
            print(f"Bunga '{nama}' Berhasil Ditambahkan!")
            input("Tekan Enter...")

        elif pilih == "2":
            print("\n=== Daftar Bunga ===")
            if not kumpulan_bunga:
                print("Belum Ada Data Bunga.")
                input("Tekan Enter...")
                continue

            table = PrettyTable(["No", "Nama Bunga", "Harga", "Stok", "Warna"])
            for i, (nama, data) in enumerate(kumpulan_bunga.items(), 1):
                table.add_row([i, nama, f"Rp {data['harga']:,}", data['stok'], data['warna']])
            print(table)
            input("Tekan Enter...")

        elif pilih == "3":
            print("=== Edit Bunga ===")
            daftar = list(kumpulan_bunga.keys())
            if not daftar:
                print("Belum Ada Data Bunga.")
                input("Tekan Enter...")
                continue

            for i, nama in enumerate(daftar, 1):
                print(f"{i}. {nama}")
            pilih_idx = input("\nPilih nomor bunga: ")
            if not pilih_idx.isdigit() or not (1 <= int(pilih_idx) <= len(daftar)):
                print("Pilihan Tidak Valid!")
                input("Tekan Enter...")
                continue

            nama_lama = daftar[int(pilih_idx) - 1]
            data = kumpulan_bunga[nama_lama]

            nama_baru = input(f"Nama baru [{nama_lama}]: ").strip() or nama_lama
            if nama_baru != nama_lama and nama_baru in kumpulan_bunga:
                print("Nama Bunga Sudah Digunakan!")
                input("Tekan Enter...")
                continue

            harga_baru = input(f"Harga baru [Rp {data['harga']:,}]: ").strip()
            if harga_baru:
                if harga_baru.isdigit():
                    harga_val = int(harga_baru)
                    if harga_val > 0 and harga_val <= 10_000_000:
                        data["harga"] = harga_val
                    else:
                        print("Harga Tidak Valid, Tidak Diubah.")
                else:
                    print("Harga Tidak Valid, Tidak Diubah.")

            stok_baru = input(f"Stok baru [{data['stok']}]: ").strip()
            if stok_baru:
                if stok_baru.isdigit():
                    stok_val = int(stok_baru)
                    if stok_val > 0:
                        data["stok"] = stok_val
                    else:
                        print("Stok tidak valid, tidak diubah.")
                else:
                    print("Stok tidak valid, tidak diubah.")

            warna_baru = input(f"Warna baru [{data['warna']}]: ").strip()
            if not warna_baru:
                warna_baru = data["warna"]
            data["warna"] = warna_baru

            if nama_baru != nama_lama:
                kumpulan_bunga[nama_baru] = kumpulan_bunga.pop(nama_lama)
                data = kumpulan_bunga[nama_baru]

            print("Data bunga berhasil diperbarui!")
            input("Tekan Enter...")

        elif pilih == "4":
            print("=== Hapus Bunga ===")
            daftar = list(kumpulan_bunga.keys())
            if not daftar:
                print("Belum ada bunga untuk dihapus.")
                input("Tekan Enter...")
                continue

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
                print("Penghapusan Dibatalkan.")
            input("Tekan Enter...")

        elif pilih == "5":
            register_admin()

        elif pilih == "6":
            print("=== RIWAYAT PEMBELIAN TOKO BUNGA HIAS ===")
            print(f"Jumlah Admin: {len(data_admin)}")
            print(f"Pengunjung Hari Ini: {jumlah_pengunjung}")
            total_stok_nilai = sum(b.get("stok", 0) for b in kumpulan_bunga.values())
            print(f"Total Stok Bunga: {total_stok_nilai:,}")
            print(f"Total Transaksi Hari Ini: Rp {total_transaksi_hari_ini:,}")
            input("\nTekan Enter...")

        elif pilih == "0":
            print("Anda Telah Logout.")
            input("Tekan Enter...")
            break
