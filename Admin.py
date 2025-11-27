from rich.console import Console
from rich.table import Table as RichTable
from rich.panel import Panel
from rich import box
import Data
from Promo import cek_input_angka

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
            peringatan("Input harus berupa angka (tanpa koma)!")
            continue
        if minimum is not None and val < minimum:
            peringatan(f"Nilai minimal: {minimum}")
            continue
        if maximum is not None and val > maximum:
            peringatan(f"Nilai maksimal: {maximum}")
            continue
        return val

def register_admin():
    console.print("\n[bold cyan]=== Daftarkan Admin Baru ===[/bold cyan]")
    nama = input_nonempty("Nama admin baru: ")
    if nama in Data.data_admin:
        gagal("Nama admin sudah digunakan!")
        input("Tekan Enter...")
        return
    password = input_nonempty("Password: ")
    Data.data_admin[nama] = password
    sukses(f"Admin '{nama}' berhasil didaftarkan!")
    input("Tekan Enter...")

def dashboard_admin(nama_admin):
    while True:
        console.print("\n" + "="*55, style="bold cyan")
        console.print(" " * 10 + "TOKO BUNGA HIAS 💐 - ADMIN", style="bold magenta")
        console.print("="*55, style="bold cyan")

        console.print("""
[bold cyan][1][/bold cyan]🌷 [white]Tambah Bunga Baru[/white]
[bold cyan][2][/bold cyan]📋 [white]Lihat Semua Bunga[/white]
[bold cyan][3][/bold cyan]♻️  [white]Edit Bunga[/white]
[bold cyan][4][/bold cyan]❌ [white]Hapus Bunga[/white]
[bold cyan][5][/bold cyan]👤 [white]Daftarkan Admin Baru[/white]
[bold cyan][6][/bold cyan]🏬 [white]Info Toko[/white]
[bold cyan][0][/bold cyan]➡️  [white]Logout[/white]
        """)
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

        if pilih == 1:
            console.print("[bold yellow]=== Tambah Bunga Baru ===[/bold yellow]")

            while True:
                nama = input_nonempty("Nama bunga: ")
                if not nama.replace(" ", "").isalnum():
                     peringatan("Nama bunga tidak boleh mengandung simbol!")
                     continue
                if nama in Data.kumpulan_bunga:
                    peringatan("Nama bunga sudah ada! Masukkan nama lain.")
                    continue
                break

            while True:
                raw_harga = input("Harga (Rp): ").strip()
                if raw_harga == "":
                    peringatan("Input tidak boleh kosong!")
                    continue
                try:
                    harga = int(raw_harga)
                    if harga <= 0 or harga > 10_000_000:
                        peringatan("Harga harus > 0 dan <= 10.000.000")
                        continue
                    break
                except Exception:
                      peringatan("Input harus berupa angka (tanpa koma)!")

            stok = input_int("Stok: ", minimum=1)
            while True :
                warna = input_nonempty("Warna: ")
                if not warna.replace(" ", "").isalpha():
                     peringatan("Warna hanya boleh huruf, dan tidak boleh mengandung angka atau simbol!")
                     continue

                Data.kumpulan_bunga[nama] = {
                    "harga": harga,
                    "stok": stok,
                    "warna": warna
                    }
            
                sukses(f"Bunga '{nama}' berhasil ditambahkan!")
                input("Tekan Enter...")
                break
        elif pilih == 2:
            if not Data.kumpulan_bunga:
                peringatan("Belum ada data bunga.")
                input("Tekan Enter...")
                continue

            tabel_bunga = RichTable(title="DAFTAR BUNGA", box=box.ROUNDED, border_style="cyan")
            tabel_bunga.add_column("No", style="bold white")
            tabel_bunga.add_column("Nama Bunga", style="bold magenta")
            tabel_bunga.add_column("Harga (Rp)", style="bold yellow")
            tabel_bunga.add_column("Stok", style="bold green")
            tabel_bunga.add_column("Warna", style="bold blue")

            for i, (nama, data) in enumerate(Data.kumpulan_bunga.items(), 1):
                tabel_bunga.add_row(
                    str(i),
                    nama,
                    f"Rp {data['harga']:,}",
                    str(data['stok']),
                    data['warna']
                )

            console.print(tabel_bunga)
            input("Tekan Enter...")

        elif pilih == 3:
            console.print("[bold yellow]=== Edit Bunga ===[/bold yellow]")
            daftar = list(Data.kumpulan_bunga.keys())

            if not daftar:
                peringatan("Belum ada data bunga.")
                input("Tekan Enter...")
                continue

            for i, nama in enumerate(daftar, 1):
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
                if not (1 <= idx <= len(daftar)):
                    peringatan("Nomor tidak valid!")
                    continue
                break

            nama_lama = daftar[idx - 1]
            data = Data.kumpulan_bunga[nama_lama]

            while True:
                    nama_baru = input(f"Nama baru [{nama_lama}]: ").strip()

                    if nama_baru == "":
                        nama_baru = nama_lama
                        break

                    if not nama_baru.replace(" ", "").isalnum():
                        peringatan("Nama tidak boleh berisi simbol!")
                        continue

                    if nama_baru != nama_lama and nama_baru in Data.kumpulan_bunga:
                        peringatan("Nama sudah digunakan oleh bunga lain!")
                        continue
                    break
            while True:
                harga_in = input(f"Harga baru [{data['harga']}]: ").strip()
                if harga_in == "":
                    harga_val = data["harga"]
                    break
                if not harga_in.isdigit():
                    peringatan("Harga harus berupa angka bulat!")
                    continue
                harga_val = int(harga_in)
                if harga_val <= 0 or harga_val > 10_000_000:
                    peringatan("Harga harus > 0 dan <= 10.000.000!")
                    continue
                break

            while True:
                stok_in = input(f"Stok baru [{data['stok']}]: ").strip()
                if stok_in == "":
                    stok_val = data["stok"]
                    break
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
                    warna_val = data["warna"]
                    break
                if not warna_in.replace(" ", "").isalpha():
                     peringatan("Warna tidak boleh berisi angka atau simbol!")
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
            daftar = list(Data.kumpulan_bunga.keys())
            if not daftar:
                peringatan("Belum ada bunga untuk dihapus.")
                input("Tekan Enter...")
                continue

            for i, nama in enumerate(daftar, 1):
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
                if not (1 <= idx <= len(daftar)):
                    peringatan("Nomor tidak valid!")
                    continue
                break

            nama_hapus = daftar[idx - 1]
            konfirm = input(f"Yakin hapus '{nama_hapus}'? (y/n): ").strip().lower()
            if konfirm == "y":
                del Data.kumpulan_bunga[nama_hapus]
                sukses(f"Bunga '{nama_hapus}' telah dihapus.")
            else:
                peringatan("Penghapusan dibatalkan.")
            input("Tekan Enter...")

        elif pilih == 5:
            register_admin()

        elif pilih == 6:
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
            input("Tekan Enter...")
            break

        else:
            peringatan("Pilihan tidak tersedia!")
            input("Tekan Enter...")
