def main_membandingkan_berat():
    berat_benda1 = float(input("Masukkan berat benda pertama (dalam gram): "))
    berat_benda2 = float(input("Masukkan berat benda kedua (dalam gram): "))

    if berat_benda1 > berat_benda2:
        print("Benda pertama lebih berat dari benda kedua.")
    elif berat_benda1 < berat_benda2:
        print("Benda kedua lebih berat dari benda pertama.")
    else:
        print("Berat kedua benda sama.")

if __name__ == "__main__":
    print("A. Membandingkan Berat Benda")
    main_membandingkan_berat()
