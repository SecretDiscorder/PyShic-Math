import math

class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

    def luas_permukaan(self):
        return 6 * self.sisi ** 2

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

    def luas_permukaan(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

class Bola:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def volume(self):
        return 4/3 * math.pi * self.jari_jari ** 3

    def luas_permukaan(self):
        return 4 * math.pi * self.jari_jari ** 2

def main():
    while True:
        print("\nMenu:")
        print("1. Hitung Volume Kubus")
        print("2. Hitung Luas Permukaan Kubus")
        print("3. Hitung Volume Balok")
        print("4. Hitung Luas Permukaan Balok")
        print("5. Hitung Volume Bola")
        print("6. Hitung Luas Permukaan Bola")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0-6): ")

        if pilihan == '1':
            sisi = float(input("Masukkan panjang sisi kubus: "))
            kubus = Kubus(sisi)
            print("Volume Kubus:", kubus.volume())
        elif pilihan == '2':
            sisi = float(input("Masukkan panjang sisi kubus: "))
            kubus = Kubus(sisi)
            print("Luas Permukaan Kubus:", kubus.luas_permukaan())
        elif pilihan == '3':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            balok = Balok(panjang, lebar, tinggi)
            print("Volume Balok:", balok.volume())
        elif pilihan == '4':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            balok = Balok(panjang, lebar, tinggi)
            print("Luas Permukaan Balok:", balok.luas_permukaan())
        elif pilihan == '5':
            jari_jari = float(input("Masukkan jari-jari bola: "))
            bola = Bola(jari_jari)
            print("Volume Bola:", bola.volume())
        elif pilihan == '6':
            jari_jari = float(input("Masukkan jari-jari bola: "))
            bola = Bola(jari_jari)
            print("Luas Permukaan Bola:", bola.luas_permukaan())
        elif pilihan == '0':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka dari 0 h
