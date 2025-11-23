from prettytable import PrettyTable
from Data import (
    kumpulan_bunga, data_pelanggan, riwayat_belanja,
    poin_member, total_transaksi_hari_ini,
    jumlah_pengunjung, diskon_member, nomor_transaksi
)
from Promo import tampilkan_promo_hari_ini, cek_input_angka, hitung_diskon, hitung_poin

import datetime
import os
import Data

from rich.console import Console
from rich.table import Table as RichTable
from rich.panel import Panel
from rich import box

console = Console()

def sukses(msg: str):
    console.print(Panel(f"[bold white]{msg}[/bold white]", title="[bold green]✔ Sukses[/bold green]", border_style="green"))

def gagal(msg: str):
    console.print(Panel(f"[bold white]{msg}[/bold white]", title="[bold red]✘ Gagal[/bold red]", border_style="red"))

def info(msg: str):
    console.print(Panel(f"[bold white]{msg}[/bold white]", title="[bold cyan]i Info[/bold cyan]", border_style="cyan"))

def peringatan(msg: str):
    console.print(Panel(f"[bold white]{msg}[/bold white]", title="[bold yellow]! Peringatan[/bold yellow]", border_style="yellow"))


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
        if not raw.isdigit():
            peringatan("Input harus angka bulat (tanpa tanda lain)!")
            continue
        val = int(raw)
        if minimum is not None and val < minimum:
            peringatan(f"Nilai minimal: {minimum}")
            continue
        if maximum is not None and val > maximum:
            peringatan(f"Nilai maksimal: {maximum}")
            continue
        return val


def buat_nomor_transaksi():
    kode = f"STK-{Data.nomor_transaksi:04d}"
    Data.nomor_transaksi += 1
    return kode

def simpan_struk_file(nama_file, isi):
    try:
        with open(nama_file, "w", encoding="utf-8") as f:
            f.write(isi)
    except OSError as e:
        gagal(f"Gagal menyimpan struk: {e}")

def cetak_struk_file(data):
    if not os.path.exists("struk"):
        try:
            os.makedirs("struk")
        except OSError as e:
            gagal(f"Gagal membuat folder struk: {e}")
            return

    isi = (
        "====================================\n"
        "           STRUK PEMBELIAN          \n"
        "====================================\n"
        f"Nomor Transaksi : {data['trx']}\n"
        f"Tanggal         : {data['tanggal']}\n"
        f"Pelanggan       : {data['pelanggan']}\n"
        "------------------------------------\n"
    )

    for item in data["keranjang"]:
        isi += f"{item['nama']} x{item['jumlah']}  Rp {item['subtotal']:,}\n"

    isi += (
        "------------------------------------\n"
        f"Subtotal        : Rp {data['subtotal']:,}\n"
        f"Diskon          : Rp {data['diskon']:,}\n"
        f"Total Bayar     : Rp {data['total']:,}\n"
        f"Poin Didapat    : {data['poin']} poin\n"
        "====================================\n"
        "     Terima kasih telah berbelanja  \n"
        "====================================\n"
    )

    nama_file = os.path.join("struk", f"{data['trx']}.txt")
    simpan_struk_file(nama_file, isi)

    console.print(Panel(isi, title=f"[bold cyan]Struk {data['trx']}[/bold cyan]", border_style="magenta"))
    sukses(f"Struk berhasil disimpan: {nama_file}")

def info_stok_tables():
    if not kumpulan_bunga:
        peringatan("Belum ada data bunga.")
        input("Tekan Enter...")
        return

    by_price = sorted(kumpulan_bunga.items(), key=lambda x: x[1].get("harga", 0))
    by_stock = sorted(kumpulan_bunga.items(), key=lambda x: x[1].get("stok", 0), reverse=True) 

    table_price = RichTable(title="Daftar Bunga — Harga Termurah → Termahal", box=box.ROUNDED, border_style="magenta")
    table_price.add_column("No", style="cyan", width=4, justify="right")
    table_price.add_column("Nama", style="bold white")
    table_price.add_column("Harga", style="yellow", justify="right")
    table_price.add_column("Stok", style="green", justify="right")
    table_price.add_column("Warna", style="bright_white", justify="center")

    for i, (nama, data) in enumerate(by_price, 1):
        table_price.add_row(str(i), nama, f"Rp {data.get('harga',0):,}", str(data.get('stok',0)), data.get('warna','-'))

    table_stock = RichTable(title="Daftar Bunga — Stok Terbanyak → Terkecil", box=box.ROUNDED, border_style="cyan")
    table_stock.add_column("No", style="cyan", width=4, justify="right")
    table_stock.add_column("Nama", style="bold white")
    table_stock.add_column("Stok", style="green", justify="right")
    table_stock.add_column("Harga", style="yellow", justify="right")
    table_stock.add_column("Warna", style="bright_white", justify="center")

    for i, (nama, data) in enumerate(by_stock, 1):
        table_stock.add_row(str(i), nama, str(data.get('stok',0)), f"Rp {data.get('harga',0):,}", data.get('warna','-'))

    console.print(Panel("[bold magenta]INFO STOK — GALAXY VIEW[/bold magenta]", border_style="bright_magenta"))

    console.print(table_price)
    console.print(table_stock)

    input("\nTekan Enter...")

def register_pelanggan():
    console.print(Panel("[bold magenta]=== Registrasi Pelanggan Baru ===[/bold magenta]", border_style="blue"))
    nama = input_nonempty("Masukkan nama: ") if 'input_nonempty' in globals() else input("Masukkan nama: ").strip()
    if not nama:
        peringatan("Nama tidak boleh kosong!")
        input("Tekan Enter...")
        return

    if nama in data_pelanggan:
        gagal("Nama sudah terdaftar, silakan login.")
        input("Tekan Enter...")
        return

    pw = input_nonempty("Masukkan password: ") if 'input_nonempty' in globals() else input("Masukkan password: ").strip()
    if not pw:
        peringatan("Password wajib diisi!")
        input("Tekan Enter...")
        return

    data_pelanggan[nama] = pw
    riwayat_belanja[nama] = []
    poin_member[nama] = 0

    sukses(f"Akun '{nama}' berhasil dibuat!")
    input("Tekan Enter...")

def dashboard_pelanggan(nama_pelanggan):

    if nama_pelanggan not in riwayat_belanja:
        riwayat_belanja[nama_pelanggan] = []
    if nama_pelanggan not in poin_member:
        poin_member[nama_pelanggan] = 0

    while True:
        console.print()
        console.print("[bold magenta]" + "╔" + "═" * 46 + "╗" + "[/bold magenta]")
        console.print("[bold cyan]" + "║" + "[/bold cyan]" + "   [bold magenta]TOKO BUNGA HIAS 💐 - PELANGGAN[/bold magenta]")
        console.print("[bold magenta]" + "╚" + "═" * 46 + "╝" + "[/bold magenta]\n")

        console.print("[bold cyan][1][/bold cyan] [white]Lihat Menu Bunga[/white]")
        console.print("[bold cyan][2][/bold cyan] [white]Belanja[/white]")
        console.print("[bold cyan][3][/bold cyan] [white]Lihat Promo[/white]")
        console.print("[bold cyan][4][/bold cyan] [white]Riwayat Belanja[/white]")
        console.print("[bold cyan][5][/bold cyan] [white]Poin Saya[/white]")
        console.print("[bold cyan][0][/bold cyan] [white]Keluar[/white]\n")

        pilih = input("Pilih menu (0-5): ").strip()
        if pilih == "":
            peringatan("Input tidak boleh kosong!")
            input("Tekan Enter...")
            continue

        if pilih == "1":
            info_stok_tables()
            continue

        elif pilih == "2":
            info_stok_tables()

            keranjang = []
            while True:
                console.print(Panel("[bold magenta]=== Tambah ke Keranjang ===[/bold magenta]", border_style="cyan"))

                daftar = [(n, d) for n, d in kumpulan_bunga.items() if d.get("stok", 0) > 0]
                if not daftar:
                    peringatan("Maaf, tidak ada bunga yang tersedia untuk dibeli.")
                    input("Enter...")
                    break

                for i, (n, d) in enumerate(daftar, 1):
                    console.print(f"[cyan]{i}[/cyan]. [white]{n}[/white] - [yellow]Rp {d.get('harga',0):,}[/yellow] (Stok: [green]{d.get('stok',0)}[/green])")

                console.print("[cyan]0[/cyan]. [white]Selesai belanja[/white]")

                pilih_idx = input("Pilih menu (angka): ").strip()
                if pilih_idx == "":
                    peringatan("Input tidak boleh kosong!")
                    continue

                if pilih_idx == "0":
                    break

                if not pilih_idx.isdigit() or not (1 <= int(pilih_idx) <= len(daftar)):
                    peringatan("Pilihan salah!")
                    continue

                nama_bunga, data_bunga = daftar[int(pilih_idx) - 1]

                try:
                    jumlah = cek_input_angka(f"Jumlah '{nama_bunga}': ")
                    if not isinstance(jumlah, int):
                        raise ValueError
                except Exception:
                    jumlah = input_int(f"Jumlah '{nama_bunga}': ", minimum=1)

                if jumlah <= 0:
                    peringatan("Jumlah harus lebih dari 0.")
                    continue

                if jumlah > data_bunga.get('stok', 0):
                    peringatan(f"Stok hanya {data_bunga.get('stok', 0)}")
                    continue

                subtotal_item = jumlah * data_bunga.get('harga', 0)

                keranjang.append({
                    "nama": nama_bunga,
                    "jumlah": jumlah,
                    "harga": data_bunga.get('harga', 0),
                    "subtotal": subtotal_item
                })

                sukses(f"{nama_bunga} ditambahkan ke keranjang!")
                input("Enter...")

            if not keranjang:
                continue

            subtotal = sum(i['subtotal'] for i in keranjang)
            total = subtotal
            diskon_poin = 0

            if poin_member.get(nama_pelanggan, 0) >= 500:
                console.print(Panel(f"[bold white]Poin kamu saat ini: {poin_member.get(nama_pelanggan,0)} poin[/bold white]",
                                    title="[bold cyan]Poin[/bold cyan]", border_style="magenta"))
                console.print("[white]Kamu bisa menukarkan poin untuk diskon:[/white]")
                console.print("[cyan]500 poin[/cyan]  → 30%")
                console.print("[cyan]1000 poin[/cyan] → 40%")
                console.print("[cyan]2000 poin[/cyan] → 50%")
                tukar = input("Apakah ingin menukarkan poin? (y/n): ").lower().strip()
                if tukar == "y":
                    if poin_member[nama_pelanggan] >= 2000:
                        diskon_poin = 0.5
                        poin_member[nama_pelanggan] -= 2000
                    elif poin_member[nama_pelanggan] >= 1000:
                        diskon_poin = 0.4
                        poin_member[nama_pelanggan] -= 1000
                    else:
                        diskon_poin = 0.3
                        poin_member[nama_pelanggan] -= 500
                    info(f"Diskon poin diterapkan: {int(diskon_poin*100)}%")
                    total = int(total * (1 - diskon_poin))

            diskon = hitung_diskon(total, diskon_member)
            total -= diskon
            poin = (total // 50000) * 100

            for item in keranjang:
                kumpulan_bunga[item['nama']]["stok"] -= item["jumlah"]

            # update langsung pakai Data.
            Data.total_transaksi_hari_ini += total
            Data.jumlah_pengunjung += 1

            trx = buat_nomor_transaksi()

            data_struk = {
                "trx": trx,
                "tanggal": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
                "pelanggan": nama_pelanggan,
                "keranjang": keranjang,
                "subtotal": subtotal,
                "diskon": diskon + int(subtotal * diskon_poin),
                "total": total,
                "poin": poin
            }

            cetak_struk_file(data_struk)

            if nama_pelanggan not in riwayat_belanja:
                riwayat_belanja[nama_pelanggan] = []
            riwayat_belanja[nama_pelanggan].append(data_struk)
            poin_member[nama_pelanggan] = poin_member.get(nama_pelanggan, 0) + poin

            sukses(f"Transaksi selesai — Total: Rp {total:,} — Poin didapat: {poin}")
            input("Enter...")

        elif pilih == "3":
            tampilkan_promo_hari_ini()
            input("Enter...")

        elif pilih == "4":
            console.print(Panel("[bold magenta]=== Riwayat Belanja ===[/bold magenta]", border_style="cyan"))
            if not riwayat_belanja.get(nama_pelanggan):
                peringatan("Belum ada riwayat.")
            else:
                for r in riwayat_belanja[nama_pelanggan]:
                    console.print(f"[cyan]{r['trx']}[/cyan] - {r['tanggal']} - [green]Rp {r['total']:,}[/green]")
            input("Enter...")

        elif pilih == "5":
            console.print(Panel(f"[bold white]Poin kamu: {poin_member.get(nama_pelanggan,0)} poin[/bold white]",
                                title="[bold cyan]Poin Saya[/bold cyan]", border_style="magenta"))
            input("Enter...")

        elif pilih == "0":
            info("Keluar dari menu pelanggan.")
            break

        else:
            peringatan("Pilihan tidak valid!")
            input("Enter...")
