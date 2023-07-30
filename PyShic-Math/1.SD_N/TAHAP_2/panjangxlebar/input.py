# BAB IV: Bangun Datar
def identifikasi_bangun_datar(nama_bangun):
    bangun_sederhana = ["persegi", "persegi panjang", "segitiga", "lingkaran", "jajar genjang", "trapesium"]
    if nama_bangun.lower() in bangun_sederhana:
        return f"{nama_bangun.capitalize()} merupakan bangun datar sederhana."
    else:
        return f"{nama_bangun.capitalize()} bukan termasuk bangun datar sederhana."

def identifikasi_jenis_sudut(degree):
    if degree < 90:
        return "Sudut lancip"
    elif degree == 90:
        return "Sudut lurus"
    elif degree > 90 and degree < 180:
        return "Sudut tumpul"
    elif degree == 180:
        return "Sudut datar"
    else:
        return "Sudut lengkung"

# BAB V: Keliling dan Luas
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_luas_bangun_datar(nama_bangun, *args):
    if nama_bangun.lower() == "persegi":
        sisi = args[0]
        return sisi * sisi
    elif nama_bangun.lower() == "persegi panjang":
        panjang = args[0]
        lebar = args[1]
        return panjang * lebar
    elif nama_bangun.lower() == "segitiga":
        alas = args[0]
        tinggi = args[1]
        return 0.5 * alas * tinggi
    elif nama_bangun.lower() == "lingkaran":
        jari_jari = args[0]
        return 3.14 * jari_jari * jari_jari
    elif nama_bangun.lower() == "jajar genjang":
        alas = args[0]
        tinggi = args[1]
        return alas * tinggi
    elif nama_bangun.lower() == "trapesium":
        sisi_a = args[0]
        sisi_b = args[1]
        tinggi = args[2]
        return 0.5 * (sisi_a + sisi_b) * tinggi
    else:
        return "Bangun datar tidak dikenali."

def main():
    print("BAB IV: Bangun Datar")
    nama_bangun = input("Masukkan nama bangun datar: ")
    print(identifikasi_bangun_datar(nama_bangun))

    print("BAB IV: Jenis Sudut")
    degree = float(input("Masukkan besar sudut dalam derajat: "))
    print(identifikasi_jenis_sudut(degree))

    print("BAB V: Keliling dan Luas")
    nama_bangun = input("Masukkan nama bangun datar (persegi, persegi panjang, segitiga, lingkaran, jajar genjang, trapesium): ")
    if nama_bangun.lower() in ["persegi", "persegi panjang"]:
        sisi_a = float(input("Masukkan panjang sisi A: "))
        sisi_b = float(input("Masukkan panjang sisi B: "))
        print(f"Keliling: {keliling_persegi_panjang(sisi_a, sisi_b)}")
        print(f"Luas: {luas_persegi_panjang(sisi_a, sisi_b)}")
    else:
        arg_names = ["alas", "tinggi", "jari-jari", "sisi A", "sisi B", "tinggi"]
        args = [float(input(f"Masukkan {arg_names[i]}: ")) for i in range(len(arg_names)) if arg_names[i] in nama_bangun]
        print(f"Luas {nama_bangun.capitalize()}: {hitung_luas_bangun_datar(nama_bangun, *args)}")

if __name__ == "__main__":
    main()
