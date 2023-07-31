def convert_seconds(seconds):
    return seconds

def convert_minutes(minutes):
    return minutes * 60

def convert_hours(hours):
    return hours * 60 * 60

def convert_days(days):
    return days * 24 * 60 * 60

def convert_years(years):
    return years * 365 * 24 * 60 * 60

def convert_decades(decades):
    return decades * 10 * 365 * 24 * 60 * 60

def convert_scores(scores):
    return scores * 20 * 365 * 24 * 60 * 60

def convert_centuries(centuries):
    return centuries * 100 * 365 * 24 * 60 * 60

def convert_moons(moons):
    return moons * 29.53059 * 24 * 60 * 60

def main():
    print("Menu Konversi Waktu:")
    print("1. Detik")
    print("2. Menit")
    print("3. Jam")
    print("4. Hari")
    print("5. Tahun")
    print("6. Dekade")
    print("7. Dasawarsa")
    print("8. Windu")
    print("9. Abad")
    print("10. Bulan")

    choice = int(input("Pilih menu (1-10): "))

    if choice == 1:
        seconds = int(input("Masukkan jumlah detik: "))
        print(f"{seconds} detik adalah {seconds} detik.")
        print(f"{seconds} detik adalah {seconds / 60} menit.")
        print(f"{seconds} detik adalah {seconds / 3600} jam.")
        print(f"{seconds} detik adalah {seconds / 86400} hari.")
        print(f"{seconds} detik adalah {seconds / (365 * 86400)} tahun.")
        print(f"{seconds} detik adalah {seconds / (10 * 365 * 86400)} dekade.")
        print(f"{seconds} detik adalah {seconds / (100 * 365 * 86400)} dasawarsa.")
        print(f"{seconds} detik adalah {seconds / (200 * 365 * 86400)} windu.")
        print(f"{seconds} detik adalah {seconds / (100 * 365 * 86400)} abad.")
        print(f"{seconds} detik adalah {seconds / (29.53059 * 24 * 60 * 60)} bulan.")

    elif choice == 2:
        minutes = int(input("Masukkan jumlah menit: "))
        print(f"{minutes} menit adalah {convert_minutes(minutes)} detik.")
        print(f"{minutes} menit adalah {minutes} menit.")
        print(f"{minutes} menit adalah {minutes / 60} jam.")
        print(f"{minutes} menit adalah {minutes / 1440} hari.")
        print(f"{minutes} menit adalah {minutes / (365 * 1440)} tahun.")
        print(f"{minutes} menit adalah {minutes / (10 * 365 * 1440)} dekade.")
        print(f"{minutes} menit adalah {minutes / (100 * 365 * 1440)} dasawarsa.")
        print(f"{minutes} menit adalah {minutes / (200 * 365 * 1440)} windu.")
        print(f"{minutes} menit adalah {minutes / (100 * 365 * 1440)} abad.")
        print(f"{minutes} menit adalah {minutes / (29.53059 * 24 * 60)} bulan.")

    elif choice == 3:
        hours = int(input("Masukkan jumlah jam: "))
        print(f"{hours} jam adalah {convert_hours(hours)} detik.")
        print(f"{hours} jam adalah {hours * 60} menit.")
        print(f"{hours} jam adalah {hours} jam.")
        print(f"{hours} jam adalah {hours / 24} hari.")
        print(f"{hours} jam adalah {hours / (365 * 24)} tahun.")
        print(f"{hours} jam adalah {hours / (10 * 365 * 24)} dekade.")
        print(f"{hours} jam adalah {hours / (100 * 365 * 24)} dasawarsa.")
        print(f"{hours} jam adalah {hours / (200 * 365 * 24)} windu.")
        print(f"{hours} jam adalah {hours / (100 * 365 * 24)} abad.")
        print(f"{hours} jam adalah {hours / (29.53059 * 24)} bulan.")

    elif choice == 4:
        days = int(input("Masukkan jumlah hari: "))
        print(f"{days} hari adalah {convert_days(days)} detik.")
        print(f"{days} hari adalah {days * 24 * 60} menit.")
        print(f"{days} hari adalah {days * 24} jam.")
        print(f"{days} hari adalah {days} hari.")
        print(f"{days} hari adalah {days / 365} tahun.")
        print(f"{days} hari adalah {days / (10 * 365)} dekade.")
        print(f"{days} hari adalah {days / (100 * 365)} dasawarsa.")
        print(f"{days} hari adalah {days / (200 * 365)} windu.")
        print(f"{days} hari adalah {days / (100 * 365)} abad.")
        print(f"{days} hari adalah {days / (29.53059)} bulan.")

    elif choice == 5:
        years = int(input("Masukkan jumlah tahun: "))
        print(f"{years} tahun adalah {convert_years(years)} detik.")
        print(f"{years} tahun adalah {years * 365 * 24 * 60} menit.")
        print(f"{years} tahun adalah {years * 365 * 24} jam.")
        print(f"{years} tahun adalah {years * 365} hari.")
        print(f"{years} tahun adalah {years} tahun.")
        print(f"{years} tahun adalah {years / 10} dekade.")
        print(f"{years} tahun adalah {years / 100} dasawarsa.")
        print(f"{years} tahun adalah {years / 200} windu.")
        print(f"{years} tahun adalah {years / 100} abad.")
        print(f"{years} tahun adalah {years / (29.53059 * 12)} bulan.")

    elif choice == 6:
        decades = int(input("Masukkan jumlah dekade: "))
        print(f"{decades} dekade adalah {convert_decades(decades)} detik.")
        print(f"{decades} dekade adalah {decades * 10 * 365 * 24 * 60} menit.")
        print(f"{decades} dekade adalah {decades * 10 * 365 * 24} jam.")
        print(f"{decades} dekade adalah {decades * 10 * 365} hari.")
        print(f"{decades} dekade adalah {decades * 10} tahun.")
        print(f"{decades} dekade adalah {decades} dekade.")
        print(f"{decades} dekade adalah {decades / 10} dasawarsa.")
        print(f"{decades} dekade adalah {decades / 20} windu.")
        print(f"{decades} dekade adalah {decades / 10} abad.")
        print(f"{decades} dekade adalah {decades / (29.53059 * 12 * 10)} bulan.")

    elif choice == 7:
        dasawarsa = int(input("Masukkan jumlah dasawarsa: "))
        print(f"{dasawarsa} dasawarsa adalah {convert_decades(dasawarsa * 10)} detik.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa * 10 * 10 * 365 * 24 * 60} menit.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa * 10 * 10 * 365 * 24} jam.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa * 10 * 10 * 365} hari.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa * 10 * 10} tahun.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa * 10} dekade.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa} dasawarsa.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa / 2} windu.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa / 10} abad.")
        print(f"{dasawarsa} dasawarsa adalah {dasawarsa / (29.53059 * 12 * 10)} bulan.")

    elif choice == 8:
        windu = int(input("Masukkan jumlah windu: "))
        print(f"{windu} windu adalah {convert_decades(windu * 200)} detik.")
        print(f"{windu} windu adalah {windu * 200 * 10 * 365 * 24 * 60} menit.")
        print(f"{windu} windu adalah {windu * 200 * 10 * 365 * 24} jam.")
        print(f"{windu} windu adalah {windu * 200 * 10 * 365} hari.")
        print(f"{windu} windu adalah {windu * 200 * 10} tahun.")
        print(f"{windu} windu adalah {windu * 20} dekade.")
        print(f"{windu} windu adalah {windu * 2} dasawarsa.")
        print(f"{windu} windu adalah {windu} windu.")
        print(f"{windu} windu adalah {windu / 5} abad.")
        print(f"{windu} windu adalah {windu / (29.53059 * 12 * 200)} bulan.")

    elif choice == 9:
        centuries = int(input("Masukkan jumlah abad: "))
        print(f"{centuries} abad adalah {convert_centuries(centuries)} detik.")
        print(f"{centuries} abad adalah {centuries * 100 * 365 * 24 * 60} menit.")
        print(f"{centuries} abad adalah {centuries * 100 * 365 * 24} jam.")
        print(f"{centuries} abad adalah {centuries * 100 * 365} hari.")
        print(f"{centuries} abad adalah {centuries * 100} tahun.")
        print(f"{centuries} abad adalah {centuries * 10} dekade.")
        print(f"{centuries} abad adalah {centuries * 2} dasawarsa.")
        print(f"{centuries} abad adalah {centuries / 2} windu.")
        print(f"{centuries} abad adalah {centuries} abad.")
        print(f"{centuries} abad adalah {centuries / (29.53059 * 12 * 100)} bulan.")

    elif choice == 10:
        moons = int(input("Masukkan jumlah bulan: "))
        print(f"{moons} bulan adalah {convert_moons(moons)} detik.")
        print(f"{moons} bulan adalah {moons * 29.53059 * 24 * 60} menit.")
        print(f"{moons} bulan adalah {moons * 29.53059 * 24} jam.")
        print(f"{moons} bulan adalah {moons * 29.53059} hari.")
        print(f"{moons} bulan adalah {moons * 29.53059 / 365} tahun.")
        print(f"{moons} bulan adalah {moons * 29.53059 / 3650} dekade.")
        print(f"{moons} bulan adalah {moons * 29.53059 / 36500} dasawarsa.")
        print(f"{moons} bulan adalah {moons * 29.53059 / 73000} windu.")
        print(f"{moons} bulan adalah {moons * 29.53059 / 36500} abad.")
        print(f"{moons} bulan adalah {moons} bulan.")

    else:
        print("Pilihan tidak valid. Silakan pilih angka menu yang benar.")

if __name__ == "__main__":
    main()
