def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def main_penjumlahan_dan_pengurangan():
    print("Penjumlahan dan Pengurangan")
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    
    hasil_penjumlahan = penjumlahan(a, b)
    hasil_pengurangan = pengurangan(a, b)

    print(f"Hasil penjumlahan: {hasil_penjumlahan}")
    print(f"Hasil pengurangan: {hasil_pengurangan}")

if __name__ == "__main__":
    main_penjumlahan_dan_pengurangan()
