# BAB III: Pecahan Sederhana
def mengenal_pecahan(pembilang, penyebut):
    return f"Pecahan {pembilang}/{penyebut} adalah pecahan sederhana."

def membandingkan_pecahan(pembilang1, penyebut1, pembilang2, penyebut2):
    pecahan1 = pembilang1 / penyebut1
    pecahan2 = pembilang2 / penyebut2
    if pecahan1 > pecahan2:
        return f"Pecahan {pembilang1}/{penyebut1} lebih besar daripada pecahan {pembilang2}/{penyebut2}."
    elif pecahan1 < pecahan2:
        return f"Pecahan {pembilang1}/{penyebut1} lebih kecil daripada pecahan {pembilang2}/{penyebut2}."
    else:
        return f"Pecahan {pembilang1}/{penyebut1} sama dengan pecahan {pembilang2}/{penyebut2}."

def pecahkan_masalah_pecahan(jumlah_benda, jumlah_total):
    pecahan = jumlah_benda / jumlah_total
    return f"{jumlah_benda} dari total {jumlah_total} benda adalah pecahan {pecahan}."

def main():
    print("BAB III: Pecahan Sederhana")
    pembilang = int(input("Masukkan pembilang pecahan: "))
    penyebut = int(input("Masukkan penyebut pecahan: "))
    print(mengenal_pecahan(pembilang, penyebut))

    pembilang1 = int(input("Masukkan pembilang pecahan pertama: "))
    penyebut1 = int(input("Masukkan penyebut pecahan pertama: "))
    pembilang2 = int(input("Masukkan pembilang pecahan kedua: "))
    penyebut2 = int(input("Masukkan penyebut pecahan kedua: "))
    print(membandingkan_pecahan(pembilang1, penyebut1, pembilang2, penyebut2))

    jumlah_benda = int(input("Masukkan jumlah benda: "))
    jumlah_total = int(input("Masukkan jumlah total benda: "))
    print(pecahkan_masalah_pecahan(jumlah_benda, jumlah_total))

if __name__ == "__main__":
    main()
