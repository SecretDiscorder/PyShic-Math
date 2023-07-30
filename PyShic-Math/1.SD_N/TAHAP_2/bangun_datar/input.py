# BAB III: Perkalian dan Pembagian
def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak dapat dilakukan."
    return a / b

# BAB IV: Bangun Datar
def mengelompokan_bangun_datar(nama_bangun):
    if nama_bangun.lower() == 'segitiga':
        return 'Segitiga adalah bangun datar dengan tiga sisi dan tiga sudut.'
    elif nama_bangun.lower() == 'persegi':
        return 'Persegi adalah bangun datar dengan empat sisi yang sama panjang dan empat sudut siku-siku.'
    elif nama_bangun.lower() == 'lingkaran':
        return 'Lingkaran adalah bangun datar dengan bentuk bulat simetris.'
    else:
        return 'Bangun datar tidak dikenali atau belum didukung.'

def sisi_bangun_datar(nama_bangun):
    if nama_bangun.lower() == 'segitiga':
        return 'Sebuah segitiga memiliki tiga sisi.'
    elif nama_bangun.lower() == 'persegi':
        return 'Sebuah persegi memiliki empat sisi.'
    elif nama_bangun.lower() == 'lingkaran':
        return 'Sebuah lingkaran tidak memiliki sisi karena merupakan bentuk bulat.'
    else:
        return 'Bangun datar tidak dikenali atau belum didukung.'

def sudut_bangun_datar(nama_bangun):
    if nama_bangun.lower() == 'segitiga':
        return 'Sebuah segitiga memiliki tiga sudut.'
    elif nama_bangun.lower() == 'persegi':
        return 'Sebuah persegi memiliki empat sudut siku-siku.'
    elif nama_bangun.lower() == 'lingkaran':
        return 'Sebuah lingkaran tidak memiliki sudut karena merupakan bentuk bulat.'
    else:
        return 'Bangun datar tidak dikenali atau belum didukung.'

def main():
    print("BAB III: Perkalian dan Pembagian")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    print(f"Hasil perkalian: {perkalian(a, b)}")
    print(f"Hasil pembagian: {pembagian(a, b)}")

    print("\nBAB IV: Bangun Datar")
    nama_bangun = input("Masukkan nama bangun datar (segitiga/persegi/lingkaran): ")
    print(mengelompokan_bangun_datar(nama_bangun))
    print(sisi_bangun_datar(nama_bangun))
    print(sudut_bangun_datar(nama_bangun))

if __name__ == "__main__":
    main()
