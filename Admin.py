from prettytable import PrettyTable
import Data
from Promo import cek_input_angka

from rich.console import Console
from rich.table import Table as RichTable  
from rich.panel import Panel
from rich import box

console = Console()

def sukses(msg: str):
    console.print(Panel(f"[bold green]✔ {msg}[/bold green]", border_style="green"))

def gagal(msg: str):
    console.print(Panel(f"[bold red]✘ {msg}[/bold red]", border_style="red"))

def info(msg: str):
    console.print(Panel(f"[bold cyan]{msg}[/bold cyan]", border_style="cyan"))

def peringatan(msg: str):
    console.print(Panel(f"[bold yellow]⚠ {msg}[/bold yellow]", border_style="yellow"))

def input_nonempty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val == "":
            peringatan("Input tidak boleh kosong!")
            continue
        return val

def input_int(prompt: str, minimum: int = None, maximum: int = None) -> int:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            peringatan("Input tidak boleh kosong!")
            continue
        try:
            val = int(raw)
        except ValueError:
            peringatan("Input harus berupa angka bulat (tanpa koma)!")
            continue
        if minimum is not None and val < minimum:
            peringatan(f"Nilai minimal: {minimum}")
            continue
        if maximum is not None and val > maximum:
            peringatan(f"Nilai maksimal: {maximum}")
            continue
        return val

def register_admin():
<<<<<<< HEAD
    console.print("\n[bold cyan]=== Daftarkan Admin Baru ===[/bold cyan]")
    nama = input_nonempty("Nama admin baru: ")
    if nama in Data.data_admin:
        gagal("Nama admin sudah digunakan!")
        input("Tekan Enter...")
        return
    password = input_nonempty("Password: ")
    Data.data_admin[nama] = password
    sukses(f"Admin '{nama}' berhasil didaftarkan!")
=======
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
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7
    input("Tekan Enter...")

def dashboard_admin(nama_admin):
    while True:
<<<<<<< HEAD
=======
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
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7

        console.print("\n")
        console.print("[bold cyan]" + "=" * 55 + "[/bold cyan]")
        console.print("[bold magenta]" + " " * 10 + "TOKO BUNGA HIAS 💐 - ADMIN" + " " * 10 + "[/bold magenta]")
        console.print("[bold cyan]" + "=" * 55 + "[/bold cyan]")

        console.print("""
                    [bold cyan][1][/bold cyan] [white]Tambah Bunga Baru[/white]
                    [bold cyan][2][/bold cyan] [white]Lihat Semua Bunga[/white]
                    [bold cyan][3][/bold cyan] [white]Edit Bunga[/white]
                    [bold cyan][4][/bold cyan] [white]Hapus Bunga[/white]
                    [bold cyan][5][/bold cyan] [white]Daftarkan Admin Baru[/white]
                    [bold cyan][6][/bold cyan] [white]Info Toko[/white]
                    [bold cyan][0][/bold cyan] [white]Logout[/white]
                    """)

        console.print("[bold cyan]" + "=" * 55 + "[/bold cyan]")

        try:
            pilih_raw = input("Pilih menu (0-6): ").strip()
            if pilih_raw == "":
                peringatan("Input tidak boleh kosong!")
                input("Tekan Enter...")
                continue
            if not pilih_raw.isdigit():
                peringatan("Input harus angka!")
                input("Tekan Enter...")
                continue
            pilih = int(pilih_raw)
            if pilih < 0 or pilih > 6:
                peringatan("Pilihan harus di antara 0 - 6!")
                input("Tekan Enter...")
                continue
        except KeyboardInterrupt:
            console.print()
            peringatan("Diinterupsi pengguna. Kembali ke menu.")
            continue

        if pilih == 1:
            console.print("[bold yellow]=== Tambah Bunga Baru ===[/bold yellow]")

            while True:
<<<<<<< HEAD
                nama = input_nonempty("Nama bunga: ")
                if nama in Data.kumpulan_bunga:
                    peringatan("Nama bunga sudah ada! Masukkan nama lain.")
                    continue
                break
=======
                nama = input("Nama Bunga: ").strip()
                if not nama:
                    print("Nama Bunga Tidak Boleh Kosong!")
                elif nama in kumpulan_bunga:
                    print("Nama Bunga Sudah Ada!")
                else:
                    break
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7

            while True:
                try:
                    harga = cek_input_angka("Harga (Rp): ")
                except Exception:

                    harga = input_int("Harga (Rp): ", minimum=1, maximum=10_000_000)
                if harga <= 0:
<<<<<<< HEAD
                    peringatan("Harga harus lebih dari 0!")
                    continue
                if harga > 10_000_000:
                    peringatan("Harga terlalu tinggi! Maksimal Rp 10.000.000")
                    continue
                break

            stok = input_int("Stok: ", minimum=1)

            warna = input_nonempty("Warna: ")

            Data.kumpulan_bunga[nama] = {"harga": harga, "stok": stok, "warna": warna}
            sukses(f"Bunga '{nama}' berhasil ditambahkan!")
            input("Tekan Enter...")

        elif pilih == 2:
            console.print("\n[bold yellow]=== Daftar Bunga ===[/bold yellow]")
            if not Data.kumpulan_bunga:
                peringatan("Belum ada data bunga.")
=======
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
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7
                input("Tekan Enter...")
                continue

            table = PrettyTable(["No", "Nama Bunga", "Harga", "Stok", "Warna"])
            for i, (nama, data) in enumerate(Data.kumpulan_bunga.items(), 1):
                table.add_row([i, nama, f"Rp {data['harga']:,}", data['stok'], data['warna']])
            print(table)
            input("Tekan Enter...")

<<<<<<< HEAD
        elif pilih == 3:
            console.print("[bold yellow]=== Edit Bunga ===[/bold yellow]")

            if not Data.kumpulan_bunga:
                peringatan("Belum ada data bunga.")
                input("Tekan Enter...")
                continue

            for i, nama in enumerate(Data.kumpulan_bunga.keys(), 1):
                console.print(f"[cyan]{i}[/cyan]. [white]{nama}[/white]")
=======
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
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7

            while True:
                try:
                    idx_raw = input("Pilih nomor bunga: ").strip()
                    if idx_raw == "":
                        peringatan("Input tidak boleh kosong!")
                        continue
                    if not idx_raw.isdigit():
                        peringatan("Input harus angka!")
                        continue
                    idx = int(idx_raw)
                    if not (1 <= idx <= len(Data.kumpulan_bunga)):
                        peringatan("Nomor tidak valid!")
                        continue
                    break
                except KeyboardInterrupt:
                    peringatan("Diinterupsi pengguna.")
                    break

<<<<<<< HEAD
            nama_lama = list(Data.kumpulan_bunga.keys())[idx - 1]
            data = Data.kumpulan_bunga[nama_lama]

            console.print(f"[bold magenta]Mengedit: {nama_lama}[/bold magenta]")
=======
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
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7

            while True:
                nama_baru = input("Nama baru [{}]: ".format(nama_lama)).strip()
                if nama_baru == "":
                    peringatan("Nama baru tidak boleh kosong! (masukkan nama baru atau ulangi nama lama)")
                    continue
                if nama_baru != nama_lama and nama_baru in Data.kumpulan_bunga:
                    peringatan("Nama sudah digunakan oleh bunga lain!")
                    continue
                break

            while True:
                harga_in = input(f"Harga baru [Rp {data['harga']:,}]: ").strip()
                if harga_in == "":
                    peringatan("Harga tidak boleh kosong!")
                    continue
                if not harga_in.isdigit():
                    peringatan("Harga harus berupa angka bulat!")
                    continue
                harga_val = int(harga_in)
                if harga_val <= 0 or harga_val > 10_000_000:
                    peringatan("Harga harus > 0 dan <= 10.000.000")
                    continue
                break

            while True:
                stok_in = input(f"Stok baru [{data['stok']}]: ").strip()
                if stok_in == "":
                    peringatan("Stok tidak boleh kosong!")
                    continue
                if not stok_in.isdigit():
                    peringatan("Stok harus berupa angka bulat!")
                    continue
                stok_val = int(stok_in)
                if stok_val <= 0:
                    peringatan("Stok harus lebih dari 0!")
                    continue
                break

            while True:
                warna_in = input(f"Warna baru [{data['warna']}]: ").strip()
                if warna_in == "":
                    peringatan("Warna tidak boleh kosong!")
                    continue
                warna_val = warna_in
                break

            if nama_baru != nama_lama:
                Data.kumpulan_bunga[nama_baru] = Data.kumpulan_bunga.pop(nama_lama)

            Data.kumpulan_bunga[nama_baru]["harga"] = harga_val
            Data.kumpulan_bunga[nama_baru]["stok"] = stok_val
            Data.kumpulan_bunga[nama_baru]["warna"] = warna_val

            sukses("Data bunga berhasil diperbarui!")
            input("Tekan Enter...")

        elif pilih == 4:
            console.print("[bold yellow]=== Hapus Bunga ===[/bold yellow]")

            if not Data.kumpulan_bunga:
                peringatan("Belum ada bunga untuk dihapus.")
                input("Tekan Enter...")
                continue

            for i, nama in enumerate(Data.kumpulan_bunga.keys(), 1):
                console.print(f"[cyan]{i}[/cyan]. [white]{nama}[/white]")

            while True:
                idx_raw = input("Pilih nomor bunga: ").strip()
                if idx_raw == "":
                    peringatan("Input tidak boleh kosong!")
                    continue
                if not idx_raw.isdigit():
                    peringatan("Input harus angka!")
                    continue
                idx = int(idx_raw)
                if not (1 <= idx <= len(Data.kumpulan_bunga)):
                    peringatan("Nomor tidak valid!")
                    continue
                break

            nama_hapus = list(Data.kumpulan_bunga.keys())[idx - 1]
            konfirm = input(f"Yakin hapus '{nama_hapus}'? (y/n): ").strip().lower()
            if konfirm == "y":
                del Data.kumpulan_bunga[nama_hapus]
                sukses(f"Bunga '{nama_hapus}' telah dihapus.")
            else:
<<<<<<< HEAD
                peringatan("Penghapusan dibatalkan.")
=======
                print("Penghapusan Dibatalkan.")
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7
            input("Tekan Enter...")

        elif pilih == 5:
            register_admin()

<<<<<<< HEAD
        elif pilih == 6:
            console.print("[bold magenta]=== INFO TOKO BUNGA HIAS ===[/bold magenta]")

            info_table = RichTable(title="INFO TOKO", box=box.ROUNDED, border_style="cyan")
            info_table.add_column("Keterangan", style="bold white")
            info_table.add_column("Nilai", style="bold yellow")

            total_stok_nilai = sum(b.get("harga", 0) * b.get("stok", 0) for b in Data.kumpulan_bunga.values())

            info_table.add_row("Jumlah Admin", str(len(Data.data_admin)))
            info_table.add_row("Pengunjung Hari Ini", str(Data.jumlah_pengunjung))
            info_table.add_row("Total Nilai Stok", f"Rp {total_stok_nilai:,}")
            info_table.add_row("Total Transaksi Hari Ini", f"Rp {Data.total_transaksi_hari_ini:,}")

            console.print(info_table)
            input("\nTekan Enter...")

        elif pilih == 0:
            console.print("[yellow]Anda telah logout.[/yellow]")
=======
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
>>>>>>> cc8d48e1a7504828db0e53371a2a550498e042d7
            input("Tekan Enter...")
            break

        else:
            peringatan("Pilihan tidak tersedia!")
            input("Tekan Enter...")
