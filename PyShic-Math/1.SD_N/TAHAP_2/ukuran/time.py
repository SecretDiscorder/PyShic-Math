def konversi_detik_ke_jam_menit_detik(detik):
    jam = detik // 3600
    sisa_detik = detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

def konversi_jam_ke_detik(jam, menit, detik):
    detik_total = (jam * 3600) + (menit * 60) + detik
    return detik_total

def main_konversi_waktu():
    print("Alat Ukur Waktu")
    print("1. Konversi Detik ke Jam, Menit, Detik")
    print("2. Konversi Jam ke Detik")
    print("3. Konversi Menit ke Detik")
    print("4. Konversi Jam, Menit, Detik ke Detik")
    pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

    if pilihan == 1:
        detik = int(input("Masukkan jumlah detik: "))
        jam, menit, detik = konversi_detik_ke_jam_menit_detik(detik)
        print(f"{detik} detik setara dengan {jam} jam, {menit} menit, dan {detik} detik.")

    elif pilihan == 2:
        jam = int(input("Masukkan jumlah jam: "))
        menit = int(input("Masukkan jumlah menit: "))
        detik = int(input("Masukkan jumlah detik: "))
        detik_total = konversi_jam_ke_detik(jam, menit, detik)
        print(f"{jam} jam, {menit} menit, dan {detik} detik setara dengan {detik_total} detik.")

    elif pilihan == 3:
        menit = int(input("Masukkan jumlah menit: "))
        detik_total = konversi_jam_ke_detik(0, menit, 0)
        print(f"{menit} menit setara dengan {detik_total} detik.")

    elif pilihan == 4:
        jam = int(input("Masukkan jumlah jam: "))
        menit = int(input("Masukkan jumlah menit: "))
        detik = int(input("Masukkan jumlah detik: "))
        detik_total = konversi_jam_ke_detik(jam, menit, detik)
        print(f"{jam} jam, {menit} menit, dan {detik} detik setara dengan {detik_total} detik.")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_konversi_waktu()
