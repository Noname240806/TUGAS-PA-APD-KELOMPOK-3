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
            if nama in data_admin:
                pw = input("Password: ").strip()
                if pw == data_admin[nama]:
                    print("Login berhasil!")
                    input("Tekan Enter...")
                    dashboard_admin(nama)
                else:
                    print("Password salah!")
                    input("Tekan Enter...")
            else:
                print("Admin tidak ditemukan!")
                input("Tekan Enter...")

        elif role == "2":
            while True:
                print("""
     =======================================================
     |                PELANGGAN MENU                      |
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
                    if nama in data_pelanggan:
                        pw = input("Password: ").strip()
                        if pw == data_pelanggan[nama]:
                            print(f"Selamat datang, {nama} 🌸")
                            input("Tekan Enter...")
                            dashboard_pelanggan(nama)
                        else:
                            print("Password salah!")
                            input("Tekan Enter...")
                    else:
                        print("Akun tidak ditemukan!")
                        input("Tekan Enter...")
                elif pilih == "0":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter...")

        elif role == "0":
            print("Terima kasih telah berkunjung ke Toko Bunga Hias 💐")
            break

if __name__ == "__main__":
    main()
