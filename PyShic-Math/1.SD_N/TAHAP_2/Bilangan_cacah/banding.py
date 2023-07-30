def membandingkan_bilangan(a, b):
    if a < b:
        return f"{a} lebih kecil dari {b}"
    elif a > b:
        return f"{a} lebih besar dari {b}"
    else:
        return f"{a} sama dengan {b}"

def main_membandingkan_bilangan():
    print("Membandingkan Bilangan")
    a = float(input("Masukkan bilangan pertama: "))
    b = float(input("Masukkan bilangan kedua: "))
    hasil = membandingkan_bilangan(a, b)
    print(hasil)

if __name__ == "__main__":
    main_membandingkan_bilangan()
