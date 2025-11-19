from prettytable import PrettyTable
from Data import (
    kumpulan_bunga, data_pelanggan, riwayat_belanja,
    poin_member, total_transaksi_hari_ini,
    jumlah_pengunjung, diskon_member, nomor_transaksi
)
from Promo import tampilkan_promo_hari_ini, cek_input_angka, hitung_diskon, hitung_poin

import datetime
import os


def buat_nomor_transaksi():
    global nomor_transaksi
    kode = f"STK-{nomor_transaksi:04d}"
    nomor_transaksi += 1
    return kode


def simpan_struk_file(nama_file, isi):
    with open(nama_file, "w", encoding="utf-8") as f:
        f.write(isi)


def cetak_struk_file(data):
    if not os.path.exists("struk"):
        os.makedirs("struk")

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

    print(isi)
    print(f"Struk berhasil disimpan: {nama_file}")


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
    riwayat_belanja[nama] = []
    poin_member[nama] = 0

    print(f"Akun '{nama}' berhasil dibuat!")
    input("Tekan Enter...")


def dashboard_pelanggan(nama_pelanggan):
    global jumlah_pengunjung, total_transaksi_hari_ini
    jumlah_pengunjung += 1

    if nama_pelanggan not in riwayat_belanja:
        riwayat_belanja[nama_pelanggan] = []
    if nama_pelanggan not in poin_member:
        poin_member[nama_pelanggan] = 0

    while True:
        print(f"""
        ==================================================
        [        TOKO BUNGA HIAS 💐 - PELANGGAN         ]
        ==================================================
        [1] Lihat Menu Bunga
        [2] Belanja (Keranjang)
        [3] Lihat Promo
        [4] Riwayat Belanja
        [5] Poin Saya
        [0] Keluar
        ==================================================
        """)

        pilih = input("Pilih menu (0-5): ").strip()

        if pilih == "1":
            table = PrettyTable(["No", "Nama", "Harga", "Stok", "Warna"])
            for i, (nama, d) in enumerate(kumpulan_bunga.items(), 1):
                if d['stok'] > 0:
                    table.add_row([i, nama, f"Rp {d['harga']:,}", d['stok'], d['warna']])
            print(table)
            input("Enter...")

        elif pilih == "2":
            keranjang = []

            while True:
                print("\n=== Tambah ke Keranjang ===")

                daftar = [(n, d) for n, d in kumpulan_bunga.items() if d["stok"] > 0]

                for i, (n, d) in enumerate(daftar, 1):
                    print(f"{i}. {n} - Rp {d['harga']:,} (Stok: {d['stok']})")

                print("0. Selesai belanja")

                pilih_idx = input("Pilih menu: ")

                if pilih_idx == "0":
                    break

                if not pilih_idx.isdigit() or not (1 <= int(pilih_idx) <= len(daftar)):
                    print("Pilihan salah!")
                    continue

                nama_bunga, data_bunga = daftar[int(pilih_idx) - 1]
                jumlah = cek_input_angka(f"Jumlah '{nama_bunga}': ")

                if jumlah > data_bunga['stok']:
                    print(f"Stok hanya {data_bunga['stok']}")
                    continue

                subtotal_item = jumlah * data_bunga['harga']

                keranjang.append({
                    "nama": nama_bunga,
                    "jumlah": jumlah,
                    "harga": data_bunga['harga'],
                    "subtotal": subtotal_item
                })

                print(f"{nama_bunga} ditambahkan ke keranjang!")
                input("Enter...")

            if not keranjang:
                print("Keranjang kosong.")
                input("Enter...")
                continue

            subtotal = sum(i['subtotal'] for i in keranjang)
            total = subtotal
            diskon_poin = 0


            if poin_member[nama_pelanggan] >= 500:
                print(f"\nPoin kamu saat ini: {poin_member[nama_pelanggan]} poin")
                print("Kamu bisa menukarkan poin untuk diskon:")
                print("500 poin  → 30%")
                print("1000 poin → 40%")
                print("2000 poin → 50%")
                tukar = input("Apakah ingin menukarkan poin? (y/n): ").lower()
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
                    print(f"Diskon poin diterapkan: {int(diskon_poin*100)}%")
                    total = int(total * (1 - diskon_poin))

            diskon = hitung_diskon(total, diskon_member)
            total -= diskon

            poin = (total // 50000) * 100

            for item in keranjang:
                kumpulan_bunga[item['nama']]["stok"] -= item["jumlah"]

            total_transaksi_hari_ini += total

            trx = buat_nomor_transaksi()

            data_struk = {
                "trx": trx,
                "tanggal": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
                "pelanggan": nama_pelanggan,
                "keranjang": keranjang,
                "subtotal": subtotal,
                "diskon": diskon + int(subtotal*diskon_poin),
                "total": total,
                "poin": poin
            }

            cetak_struk_file(data_struk)

            riwayat_belanja[nama_pelanggan].append(data_struk)
            poin_member[nama_pelanggan] += poin

            input("Enter...")

        elif pilih == "3":
            tampilkan_promo_hari_ini()
            input("Enter...")

        elif pilih == "4":
            print("\n=== Riwayat Belanja ===")
            if not riwayat_belanja[nama_pelanggan]:
                print("Belum ada riwayat.")
            else:
                for r in riwayat_belanja[nama_pelanggan]:
                    print(f"{r['trx']} - {r['tanggal']} - Rp {r['total']:,}")
            input("Enter...")

        elif pilih == "5":
            print(f"\nPoin kamu: {poin_member[nama_pelanggan]} poin")
            input("Enter...")

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid!")
            input("Enter...")