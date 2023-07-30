import math

def menghitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def menghitung_luas_segi_empat(panjang, lebar):
    return panjang * lebar

def menghitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def main_mengenal_bangun_datar():
    print("Mengenal Segitiga, Segi Empat, dan Lingkaran")
    print("1. Menghitung Luas Segitiga")
    print("2. Menghitung Luas Segi Empat")
    print("3. Menghitung Luas Lingkaran")

    pilihan = input("Pilih bangun datar (1/2/3): ")

    if pilihan == '1':
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = menghitung_luas_segitiga(alas, tinggi)
        print(f"Luas segitiga: {luas}")
    elif pilihan == '2':
        panjang = float(input("Masukkan panjang segi empat: "))
        lebar = float(input("Masukkan lebar segi empat: "))
        luas = menghitung_luas_segi_empat(panjang, lebar)
        print(f"Luas segi empat: {luas}")
    elif pilihan == '3':
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = menghitung_luas_lingkaran(jari_jari)
        print(f"Luas lingkaran: {luas}")
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main_mengenal_bangun_datar()
