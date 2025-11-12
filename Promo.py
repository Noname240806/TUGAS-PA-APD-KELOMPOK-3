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


def hitung_diskon(total_belanja, diskon_member):
    if total_belanja > 50000:
        return int(total_belanja * diskon_member)
    return 0
