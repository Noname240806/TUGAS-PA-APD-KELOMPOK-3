from Admin import dashboard_admin
from Pelanggan import dashboard_pelanggan, register_pelanggan
from Data import data_admin, data_pelanggan

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
        role = input("Pilih (0-2): ").strip()

        if role == "1":
            print("\n=== LOGIN ADMIN ===")
            nama = input("Nama admin: ").strip()

            if nama not in data_admin:
                print("Admin Tidak Ditemukan!")
                input("Tekan Enter...")
                continue

            percobaan = 3
            while percobaan > 0:
                pw = input(f"Password ({percobaan}): ").strip()
                if pw == data_admin[nama]:
                    print("Login Berhasil!")
                    input("Tekan Enter...")
                    dashboard_admin(nama)
                    break
                else:
                    percobaan -= 1
                    print("Password Anda Salah! Silahkan Coba Lagi")

            if percobaan == 0:
                print("Kesempatan Login Anda Telah Habis!")
                input("Tekan Enter...")

        elif role == "2":
            while True:
                print("""
     =======================================================
     |                MENU PELANGGAN                       |
     =======================================================
     | [1] Registrasi                                      |
     | [2] Login                                           |
     | [0] Kembali                                         |
     =======================================================
                """)
                pilih = input("Pilih (0-2): ").strip()

                if pilih == "1":
                    register_pelanggan()

                elif pilih == "2":
                    nama = input("Nama: ").strip()

                    if nama not in data_pelanggan:
                        print("Akun Tidak Ditemukan!")
                        input("Tekan Enter...")
                        continue

                    percobaan = 3
                    while percobaan > 0:
                        pw = input(f"Password ({percobaan}): ").strip()
                        if pw == data_pelanggan[nama]:
                            print(f"Selamat Datang, {nama} 🌸")
                            input("Tekan Enter...")
                            dashboard_pelanggan(nama)
                            break
                        else:
                            percobaan -= 1
                            print("Password Anda Salah! Silahkan Coba Lagi")

                    if percobaan == 0:
                        print("Kesempatan Login Anda Telah Habis!")
                        input("Tekan Enter...")

                elif pilih == "0":
                    break
                else:
                    print("Pilihan Tidak Valid!")
                    input("Tekan Enter...")

        elif role == "0":
            print("Terima Kasih Telah Berkunjung Ke Toko Bunga Hias 💐")
            break

if __name__ == "__main__":
    main()
