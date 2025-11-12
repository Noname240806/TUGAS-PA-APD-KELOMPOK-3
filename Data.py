from prettytable import PrettyTable

kumpulan_bunga = {
    "Mawar Merah": {"harga": 15000, "stok": 50, "warna": "Merah"},
    "Anggrek Putih": {"harga": 25000, "stok": 30, "warna": "Putih"},
    "Tulip Kuning": {"harga": 20000, "stok": 40, "warna": "Kuning"},
    "Lily Merah Muda": {"harga": 30000, "stok": 25, "warna": "Merah Muda"},
    "Krisan Ungu": {"harga": 18000, "stok": 35, "warna": "Ungu"},
    "Melati Putih": {"harga": 12000, "stok": 60, "warna": "Putih"},
    "Gerbera Oranye": {"harga": 22000, "stok": 45, "warna": "Oranye"},
}

data_admin = {"admin": "404"}
data_pelanggan = {}

# Variabel global
total_transaksi_hari_ini = 0
jumlah_pengunjung = 0
diskon_member = 0.05
