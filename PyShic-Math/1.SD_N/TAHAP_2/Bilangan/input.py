# BAB I: Bilangan
def letak_bilangan_garis_bilangan(bilangan):
    if bilangan == 0:
        return "Bilangan 0 berada pada titik tengah garis bilangan."
    elif bilangan > 0:
        return f"Bilangan {bilangan} berada di sebelah kanan titik 0 pada garis bilangan."
    else:
        return f"Bilangan {bilangan} berada di sebelah kiri titik 0 pada garis bilangan."

def penjumlahan_tiga_angka(a, b, c):
    return a + b + c

def pengurangan_tiga_angka(a, b, c):
    return a - b - c

def operasi_hitung_campuran(a, b, c):
    return (a + b) * c - (a - b) / c

def pecahkan_masalah_uang(jumlah_uang, harga_barang):
    kembalian = jumlah_uang - harga_barang
    if kembalian >= 0:
        return f"Uang Anda cukup. Kembalian: {kembalian}"
    else:
        return f"Uang Anda kurang. Kekurangan: {abs(kembalian)}"

# BAB II: Pengukuran
def pilih_alat_ukur(benda_diukur):
    if benda_diukur.lower() == 'panjang':
        return 'Alat ukur yang sesuai untuk mengukur panjang adalah meteran.'
    elif benda_diukur.lower() == 'berat':
        return 'Alat ukur yang sesuai untuk mengukur berat adalah timbangan.'
    elif benda_diukur.lower() == 'waktu':
        return 'Alat ukur yang sesuai untuk mengukur waktu adalah jam.'
    else:
        return 'Benda yang diukur tidak dikenali atau belum didukung.'

def alat_ukur_dalam_pemecahan_masalah(benda_diukur, ukuran):
    if benda_diukur.lower() == 'panjang':
        return f"{ukuran} meter adalah ukuran yang sesuai untuk menggunakan meteran dalam pemecahan masalah panjang."
    elif benda_diukur.lower() == 'berat':
        return f"{ukuran} kilogram adalah ukuran yang sesuai untuk menggunakan timbangan dalam pemecahan masalah berat."
    elif benda_diukur.lower() == 'waktu':
        return f"{ukuran} jam adalah ukuran yang sesuai untuk menggunakan jam dalam pemecahan masalah waktu."
    else:
        return 'Benda yang diukur tidak dikenali atau belum didukung.'

def hubungan_antarsatuan(ukuran, satuan_awal, satuan_tujuan):
    satuan_waktu = ['detik', 'menit', 'jam']
    satuan_panjang = ['milimeter', 'sentimeter', 'desimeter', 'meter', 'kilometer']
    satuan_berat = ['gram', 'kilogram', 'ton']

    if satuan_awal in satuan_waktu and satuan_tujuan in satuan_waktu:
        return 'Konversi waktu ke waktu belum didukung.'
    elif satuan_awal in satuan_panjang and satuan_tujuan in satuan_panjang:
        return 'Konversi panjang ke panjang belum didukung.'
    elif satuan_awal in satuan_berat and satuan_tujuan in satuan_berat:
        return 'Konversi berat ke berat belum didukung.'
    else:
        return 'Konversi antar satuan tidak valid atau belum didukung.'

def main():
    print("BAB I: Bilangan")
    bilangan = float(input("Masukkan bilangan: "))
    print(letak_bilangan_garis_bilangan(bilangan))

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    c = float(input("Masukkan angka ketiga: "))
    print(f"Hasil penjumlahan tiga angka: {penjumlahan_tiga_angka(a, b, c)}")
    print(f"Hasil pengurangan tiga angka: {pengurangan_tiga_angka(a, b, c)}")
    print(f"Hasil operasi hitung campuran: {operasi_hitung_campuran(a, b, c)}")

    jumlah_uang = float(input("Masukkan jumlah uang: "))
    harga_barang = float(input("Masukkan harga barang: "))
    print(pecahkan_masalah_uang(jumlah_uang, harga_barang))

    print("\nBAB II: Pengukuran")
    benda_diukur = input("Masukkan benda yang diukur (panjang/berat/waktu): ")
    print(pilih_alat_ukur(benda_diukur))

    ukuran = float(input("Masukkan ukuran: "))
    print(alat_ukur_dalam_pemecahan_masalah(benda_diukur, ukuran))

    satuan_awal = input("Masukkan satuan awal: ")
    satuan_tujuan = input("Masukkan satuan tujuan: ")
    print(hubungan_antarsatuan(ukuran, satuan_awal, satuan_tujuan))

if __name__ == "__main__":
    main()
