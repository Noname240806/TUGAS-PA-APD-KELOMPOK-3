from rich.console import Console
from rich.table import Table as RichTable
from rich.panel import Panel
from rich import box
from Admin import dashboard_admin
from Pelanggan import dashboard_pelanggan, register_pelanggan
from Data import data_admin, data_pelanggan

console = Console()

def sukses(msg: str):
    console.print(Panel(f"[bold green]✔ {msg}[/bold green]", border_style="green"))

def gagal(msg: str):
    console.print(Panel(f"[bold red]✘ {msg}[/bold red]", border_style="red"))

def info(msg: str):
    console.print(Panel(f"[bold cyan]{msg}[/bold cyan]", border_style="cyan"))

def peringatan(msg: str):
    console.print(Panel(f"[bold yellow]⚠ {msg}[/bold yellow]", border_style="yellow"))

def tampil_menu_utama():
    table = RichTable(title="PILIH ROLE KAMU", box=box.ROUNDED, border_style="cyan")
    table.add_column("No", justify="center", style="bold white")
    table.add_column("Role", style="bold magenta")
    table.add_column("Keterangan", style="bold yellow")
    table.add_row("1", "Admin", "Masuk sebagai admin toko bunga")
    table.add_row("2", "Pelanggan", "Masuk sebagai pelanggan")
    table.add_row("0", "Keluar", "Keluar dari program")
    console.print(table)

def tampil_menu_pelanggan():
    table = RichTable(title="MENU PELANGGAN", box=box.ROUNDED, border_style="cyan")
    table.add_column("No", justify="center", style="bold white")
    table.add_column("Aksi", style="bold magenta")
    table.add_column("Keterangan", style="bold yellow")
    table.add_row("1", "Registrasi", "Buat akun pelanggan baru")
    table.add_row("2", "Login", "Masuk sebagai pelanggan")
    table.add_row("0", "Kembali", "Kembali ke menu utama")
    console.print(table)

def main():
    while True:
        tampil_menu_utama()
        role = input("Pilih (0-2): ").strip()

        if role == "1":
            console.print("\n[bold cyan]=== LOGIN ADMIN ===[/bold cyan]")
            nama = input("Nama admin: ").strip()

            if nama not in data_admin:
                gagal("Admin Tidak Ditemukan!")
                input("Tekan Enter...")
                continue

            percobaan = 3
            while percobaan > 0:
                pw = input(f"Password: ").strip()
                if pw == data_admin[nama]:
                    sukses("Login Berhasil!")
                    input("Tekan Enter...")
                    dashboard_admin(nama)
                    break
                else:
                    percobaan -= 1
                    peringatan(f"Password Anda Salah! Sisa percobaan: {percobaan}")

            if percobaan == 0:
                gagal("Kesempatan Login Anda Telah Habis!")
                input("Tekan Enter...")

        elif role == "2":
            while True:
                tampil_menu_pelanggan()
                pilih = input("Pilih (0-2): ").strip()

                if pilih == "1":
                    register_pelanggan()

                elif pilih == "2":
                    nama = input("Nama: ").strip()

                    if nama not in data_pelanggan:
                        gagal("Akun Tidak Ditemukan!")
                        input("Tekan Enter...")
                        continue

                    percobaan = 3
                    while percobaan > 0:
                        pw = input(f"Password : ").strip()
                        if pw == data_pelanggan[nama]:
                            sukses(f"Selamat Datang, {nama} 🌸")
                            input("Tekan Enter...")
                            dashboard_pelanggan(nama)
                            break
                        else:
                            percobaan -= 1
                            peringatan(f"Password Anda Salah! Sisa percobaan: {percobaan}")

                    if percobaan == 0:
                        gagal("Kesempatan Login Anda Telah Habis!")
                        input("Tekan Enter...")

                elif pilih == "0":
                    break
                else:
                    peringatan("Pilihan Tidak Valid!")
                    input("Tekan Enter...")

        elif role == "0":
            info("Terima Kasih Telah Berkunjung Ke Toko Bunga Hias 💐")
            break

if __name__ == "__main__":
    main()
