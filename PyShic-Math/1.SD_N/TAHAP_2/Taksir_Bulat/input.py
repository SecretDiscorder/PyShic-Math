# Membulatkan bilangan ke dalam pecahan terdekat
def bulatkan_ke_pecahan(bilangan):
    pecahan_terdekat = round(bilangan * 2) / 2
    return pecahan_terdekat

# Membulatkan bilangan ke dalam ratusan terdekat
def bulatkan_ke_ratusan(bilangan):
    ratusan_terdekat = round(bilangan / 100) * 100
    return ratusan_terdekat

# Membulatkan bilangan ke dalam ribuan terdekat
def bulatkan_ke_ribuan(bilangan):
    ribuan_terdekat = round(bilangan / 1000) * 1000
    return ribuan_terdekat

# Menaksir hasil operasi hitung
def taksir_hasil_operasi(operator, a, b):
    if operator == "+":
        hasil = a + b
    elif operator == "-":
        hasil = a - b
    elif operator == "*":
        hasil = a * b
    elif operator == "/":
        hasil = a / b
    else:
        hasil = None
    return hasil

# Memecahkan masalah yang melibatkan uang
def pecahkan_masalah_uang(jumlah_uang, harga_barang):
    jumlah_barang_dibeli = jumlah_uang // harga_barang
    kembalian = jumlah_uang % harga_barang
    return jumlah_barang_dibeli, kembalian

def main_menaksir_dan_membulatkan():
    print("Menaksir dan Membulatkan Bilangan")
    print("1. Membulatkan Bilangan ke dalam Pecahan Terdekat")
    print("2. Membulatkan Bilangan ke dalam Ratusan Terdekat")
    print("3. Membulatkan Bilangan ke dalam Ribuan Terdekat")
    print("4. Menaksir Hasil Operasi Hitung")
    print("5. Memecahkan Masalah yang Melibatkan Uang")
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))

    if pilihan == 1:
        bilangan = float(input("Masukkan bilangan: "))
        pecahan_terdekat = bulatkan_ke_pecahan(bilangan)
        print(f"{bilangan} dibulatkan ke dalam pecahan terdekat: {pecahan_terdekat}")

    elif pilihan == 2:
        bilangan = float(input("Masukkan bilangan: "))
        ratusan_terdekat = bulatkan_ke_ratusan(bilangan)
        print(f"{bilangan} dibulatkan ke dalam ratusan terdekat: {ratusan_terdekat}")

    elif pilihan == 3:
        bilangan = float(input("Masukkan bilangan: "))
        ribuan_terdekat = bulatkan_ke_ribuan(bilangan)
        print(f"{bilangan} dibulatkan ke dalam ribuan terdekat: {ribuan_terdekat}")

    elif pilihan == 4:
        operator = input("Masukkan operator (+, -, *, /): ")
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        hasil_taksiran = taksir_hasil_operasi(operator, a, b)
        print(f"Hasil taksiran {a} {operator} {b}: {hasil_taksiran}")

    elif pilihan == 5:
        jumlah_uang = int(input("Masukkan jumlah uang yang dimiliki: "))
        harga_barang = int(input("Masukkan harga barang: "))
        jumlah_barang_dibeli, kembalian = pecahkan_masalah_uang(jumlah_uang, harga_barang)
        print(f"Jumlah barang yang dapat dibeli: {jumlah_barang_dibeli}")
        print(f"Kembalian: {kembalian}")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_menaksir_dan_membulatkan()
