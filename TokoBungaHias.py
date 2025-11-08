print("""
     =======================================================
     |      Selamat Datang di Toko Bunga Hias 💐          |
     =======================================================
    """)

kumpulan_bunga = {}
total_transaksi_hari_ini = 0
jumlah_pengunjung = 0
diskon_member = 0.05
data_admin = {}

if "admin" not in data_admin:
    data_admin["admin"] = "404"

if not kumpulan_bunga:
    kumpulan_bunga.update({
        "Mawar Merah": {"harga": 15000, "stok": 50, "warna": "Merah"},
        "Anggrek Putih": {"harga": 25000, "stok": 30, "warna": "Putih"},
        "Tulip Kuning": {"harga": 20000, "stok": 40, "warna": "Kuning"},
        "Lily Merah Muda": {"harga": 30000, "stok": 25, "warna": "Merah Muda"},
        "Krisan Ungu": {"harga": 18000, "stok": 35, "warna": "Ungu"},
        "Melati Putih": {"harga": 12000, "stok": 60, "warna": "Putih"},
        "Gerbera Oranye": {"harga": 22000, "stok": 45, "warna": "Oranye"}
    })



def tampilkan_promo_hari_ini():
    print("\n 🌸 PROMO HARI INI 🌸")
    print("Diskon 5% untuk pembelian di atas Rp50.000")
    print("Gratis kartu ucapan untuk setiap pembelian!")

def cek_input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit():
            return int(nilai)
        print("Input harus angka! Coba lagi.")

def validasi_stok(nama_bunga, jumlah):
    if nama_bunga not in kumpulan_bunga:
        print(f"Bunga '{nama_bunga}' tidak tersedia.")
        return False
    stok = kumpulan_bunga[nama_bunga]["stok"]
    if jumlah > stok:
        print(f"Maaf, stok hanya {stok}!")
        return False
    return True

def cari_bunga(kata_kunci):
    """Cari bunga berdasarkan nama (abaikan huruf besar/kecil)"""
    hasil = []
    kata_kunci = kata_kunci.lower().strip()
    for nama, data in kumpulan_bunga.items():
        if data["stok"] > 0 and kata_kunci in nama.lower():
            hasil.append((nama, data))
    return hasil

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
    global jumlah_pengunjung, total_transaksi_hari_ini
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
            if harga <= 0 or stok < 0:
                print("Harga harus > 0 dan stok tidak boleh negatif!")
            else:
                kumpulan_bunga[nama] = {"harga": harga, "stok": stok, "warna": warna}
                print(f"Bunga '{nama}' berhasil ditambahkan!")
            input("Tekan Enter...")

        elif pilih == "2":
            print("=== Daftar Bunga ===")
            if not kumpulan_bunga:
                print("Belum ada bunga di toko.")
            else:
                for i, (nama, data) in enumerate(kumpulan_bunga.items(), 1):
                    print(f"{i}. {nama}")
                    print(f"   Harga: Rp {data['harga']:,}")
                    print(f"   Stok: {data['stok']}")
                    print(f"   Warna: {data['warna']}\n")
            input("Tekan Enter...")

        elif pilih == "3":
            print("=== Edit Bunga ===")
            if not kumpulan_bunga:
                print("Tidak ada bunga untuk diedit.")
                input("Tekan Enter...")
                continue
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
            print(f"\nMengedit: {nama_lama}")
            nama_baru = input(f"Nama baru [{nama_lama}]: ").strip() or nama_lama
            harga_baru = input(f"Harga baru [Rp {data['harga']:,}]: ").strip()
            stok_baru = input(f"Stok baru [{data['stok']}]: ").strip()
            warna_baru = input(f"Warna baru [{data['warna']}]: ").strip() or data["warna"]

            if nama_baru != nama_lama:
                kumpulan_bunga[nama_baru] = kumpulan_bunga.pop(nama_lama)
                data = kumpulan_bunga[nama_baru]

            if harga_baru.isdigit():
                data["harga"] = int(harga_baru)
            # Update stok
            if stok_baru.isdigit():
                data["stok"] = int(stok_baru)

            data["warna"] = warna_baru

            print("Data bunga berhasil diperbarui!")
            input("Tekan Enter...")

        elif pilih == "4":
            print("=== Hapus Bunga ===")
            if not kumpulan_bunga:
                print("Tidak ada bunga untuk dihapus.")
                input("Tekan Enter...")
                continue
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

        else:
            print("Pilihan tidak valid!")
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
        [2] Cari Bunga
        [3] Beli Bunga
        [4] Lihat Promo
        [0] Keluar
        ==================================================
        """)
        pilih = input("Pilih menu (0-4): ").strip()

        if pilih == "1":
            print("=== Menu Bunga Tersedia ===")
            if not kumpulan_bunga:
                print("Maaf, toko sedang kosong.")
            else:
                tersedia = False
                for nama, data in kumpulan_bunga.items():
                    if data["stok"] > 0:
                        tersedia = True
                        print(f"🌸 {nama}")
                        print(f"   Harga: Rp {data['harga']:,}")
                        print(f"   Stok: {data['stok']}")
                        print(f"   Warna: {data['warna']}\n")
                if not tersedia:
                    print("Maaf, semua bunga sedang kosong.")
            input("Tekan Enter...")

        elif pilih == "2": 

            print("=== Cari Bunga ===")
            if not kumpulan_bunga:
                print("Toko sedang kosong.")
                input("Tekan Enter...")
                continue
            
            kata_kunci = input("Masukkan nama bunga yang dicari: ").strip()
            if not kata_kunci:
                print("Kata kunci tidak boleh kosong!")
                input("Tekan Enter...")
                continue

            hasil = cari_bunga(kata_kunci)
            if hasil:
                print(f"\nDitemukan {len(hasil)} bunga:")
                for i, (nama, data) in enumerate(hasil, 1):
                    print(f"{i}. {nama}")
                    print(f"   Harga: Rp {data['harga']:,}")
                    print(f"   Stok: {data['stok']}")
                    print(f"   Warna: {data['warna']}\n")
            else:
                print(f"\n❌ Bunga '{kata_kunci}' tidak ditemukan atau stok habis.")
            input("Tekan Enter...")

        elif pilih == "3":
            print("=== Beli Bunga ===")
            if not kumpulan_bunga:
                print("Toko sedang kosong.")
                input("Tekan Enter...")
                continue

            daftar_tersedia = [(nama, data) for nama, data in kumpulan_bunga.items() if data["stok"] > 0]
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
            if not validasi_stok(nama_beli, jumlah):
                input("Tekan Enter...")
                continue

            subtotal = data_bunga["harga"] * jumlah
            diskon = hitung_diskon(subtotal)
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
            print("\nTerima kasih telah berbelanja di toko bunga ini! 🌸")
            input("\nTekan Enter...")

        elif pilih == "4":
            tampilkan_promo_hari_ini()
            input("\nTekan Enter...")

        elif pilih == "0":
            print("Terima kasih telah berkunjung, sampai jumpa!")
            input("Tekan Enter...")
            break

        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

def hitung_diskon(total_belanja):
    if total_belanja > 50000:
        return int(total_belanja * diskon_member)
    return 0

def main():
    while True:
        print("""
     =======================================================
     |               PILIH ROLE KAMU ?                     |
     =======================================================
     | [1] Admin                                           |
     | [2] Pelanggan                                       |
     | [0] Keluar                                          |
     =======================================================
        """)
        role_pilih = input("Pilih (0-2): ").strip()

        if role_pilih == "1":
            while True:
                print("""
     =======================================================
     |                MASUK SEBAGAI ADMIN                  |
     =======================================================
     | [1] Login                                           |
     | [2] Kembali ke Pemilihan Role                       |
     =======================================================
                """)
                p = input("Pilih (1/2): ").strip()
                if p == "1":
                    nama = input("Nama admin: ").strip()
                    if nama in data_admin:
                        pw = input("Password: ")
                        if pw == data_admin[nama]:
                            print("Login berhasil!")
                            input("Tekan Enter untuk masuk dashboard...")
                            dashboard_admin(nama)
                            break
                        else:
                            print("Password salah!")
                            input("Tekan Enter...")
                    else:
                        print("Admin tidak ditemukan.")
                        input("Tekan Enter...")
                elif p == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter...")

        elif role_pilih == "2":
            print("=== Selamat Datang, Pelanggan! ===")
            nama = input("Silakan masukkan nama Anda: ").strip()
            if not nama:
                nama = "Pelanggan"
            print(f"Hai, {nama}! Selamat berbelanja di Toko Bunga Hias  🌸")
            input("Tekan Enter untuk melanjutkan...")
            dashboard_pelanggan(nama)

        elif role_pilih == "0":
            print("Terima kasih telah mengunjungi Toko Bunga Hias ini! 🌺")
            break

        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

if __name__ == "__main__":
    main()