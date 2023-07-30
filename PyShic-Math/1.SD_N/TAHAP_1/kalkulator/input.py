def membilang_banyak_benda(jumlah_benda):
    if jumlah_benda == 1:
        return "satu"
    elif jumlah_benda == 2:
        return "dua"
    elif jumlah_benda == 3:
        return "tiga"
    elif jumlah_benda == 4:
        return "empat"
    elif jumlah_benda == 5:
        return "lima"
    # dan seterusnya hingga 9
    else:
        return "banyak"  # untuk jumlah benda lebih dari 9

def main_membilang_banyak_benda():
    jumlah_benda = int(input("Masukkan jumlah benda: "))
    hasil = membilang_banyak_benda(jumlah_benda)
    print(f"{jumlah_benda} benda: {hasil}")

def jumlahkan(angka1, angka2):
    return angka1 + angka2

def kurangkan(angka1, angka2):
    return angka1 - angka2

def main_jumlah_kurang():
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil_jumlah = jumlahkan(angka1, angka2)
    hasil_kurang = kurangkan(angka1, angka2)

    print(f"{angka1} + {angka2} = {hasil_jumlah}")
    print(f"{angka1} - {angka2} = {hasil_kurang}")

def pertukaran_dan_pengelompokan(a, b):
    # Operasi pertukaran nilai a dan b
    a, b = b, a

    # Operasi pengelompokan
    c = a + b
    d = a - b

    return a, b, c, d

def main_pertukaran_pengelompokan():
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil_a, hasil_b, hasil_c, hasil_d = pertukaran_dan_pengelompokan(angka1, angka2)

    print(f"Hasil pertukaran: a = {hasil_a}, b = {hasil_b}")
    print(f"Hasil pengelompokan: c = {hasil_c}, d = {hasil_d}")

def main():
    print("A. Membilang Banyak Benda")
    main_membilang_banyak_benda()
    print("\nB. Menjumlahkan Dan Mengurangkan")
    main_jumlah_kurang()
    print("\nC. Sifat-Sifat Operasi Pertukaran Dan Pengelompokan")
    main_pertukaran_pengelompokan()

if __name__ == "__main__":
    main()
