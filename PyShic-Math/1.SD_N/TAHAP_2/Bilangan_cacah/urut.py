def mengurutkan_bilangan(a, b, c):
    bilangan = [a, b, c]
    bilangan.sort()
    return bilangan

def main_mengurutkan_bilangan():
    print("Mengurutkan Bilangan")
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    c = float(input("Masukkan bilangan ketiga: "))
    hasil = mengurutkan_bilangan(a, b, c)
    print("Bilangan terurut:", hasil)

if __name__ == "__main__":
    main_mengurutkan_bilangan()
