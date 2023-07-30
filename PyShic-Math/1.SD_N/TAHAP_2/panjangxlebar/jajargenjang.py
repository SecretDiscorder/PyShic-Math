# Function to calculate the perimeter of a jajar genjang
def keliling_jajar_genjang(a, b):
    return 2 * (a + b)

# Function to calculate the area of a jajar genjang
def luas_jajar_genjang(a, t):
    return a * t

# Function to calculate the perimeter of a triangle
def keliling_segitiga(a, b, c):
    return a + b + c

# Function to calculate the area of a triangle
def luas_segitiga(a, t):
    return 0.5 * a * t

def main_keliling_dan_luas():
    print("1. Keliling dan Luas Jajar Genjang")
    print("2. Keliling dan Luas Segitiga")
    pilihan = int(input("Masukkan pilihan (1/2): "))

    if pilihan == 1:
        a = float(input("Masukkan panjang sisi atas (a) jajar genjang: "))
        b = float(input("Masukkan panjang sisi bawah (b) jajar genjang: "))
        t = float(input("Masukkan tinggi (t) jajar genjang: "))

        keliling = keliling_jajar_genjang(a, b)
        luas = luas_jajar_genjang(a, t)

        print(f"Keliling jajar genjang adalah {keliling:.2f} satuan panjang.")
        print(f"Luas jajar genjang adalah {luas:.2f} satuan luas.")

    elif pilihan == 2:
        a = float(input("Masukkan panjang sisi pertama (a) segitiga: "))
        b = float(input("Masukkan panjang sisi kedua (b) segitiga: "))
        c = float(input("Masukkan panjang sisi ketiga (c) segitiga: "))
        t = float(input("Masukkan tinggi (t) segitiga: "))

        keliling = keliling_segitiga(a, b, c)
        luas = luas_segitiga(a, t)

        print(f"Keliling segitiga adalah {keliling:.2f} satuan panjang.")
        print(f"Luas segitiga adalah {luas:.2f} satuan luas.")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_keliling_dan_luas()
