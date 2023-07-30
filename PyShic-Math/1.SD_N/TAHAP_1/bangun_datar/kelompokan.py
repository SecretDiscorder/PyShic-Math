def mengelompokkan_bangun_datar(jenis_bangun):
    segitiga = ["segitiga", "segitiga sama sisi", "segitiga sama kaki"]
    segi_empat = ["segi empat", "persegi", "persegi panjang"]
    lingkaran = ["lingkaran"]

    if jenis_bangun.lower() in segitiga:
        return "Segitiga"
    elif jenis_bangun.lower() in segi_empat:
        return "Segi Empat"
    elif jenis_bangun.lower() in lingkaran:
        return "Lingkaran"
    else:
        return "Bangun datar tidak dikenal."

def main_mengelompokkan_bangun_datar():
    print("Mengelompokkan Bangun Datar")
    jenis_bangun = input("Masukkan jenis bangun datar: ")
    kelompok = mengelompokkan_bangun_datar(jenis_bangun)
    print(f"{jenis_bangun.capitalize()} termasuk dalam kelompok {kelompok}.")

if __name__ == "__main__":
    main_mengelompokkan_bangun_datar()
