import datetime

def main():
    input_date = input("Masukkan tanggal (YYYY-MM-DD): ")
    input_time = input("Masukkan jam (HH:MM:SS): ")

    try:
        year, month, day = map(int, input_date.split('-'))
        hour, minute, second = map(int, input_time.split(':'))

        waktu = datetime.datetime(year, month, day, hour, minute, second)

        # Mendapatkan nama hari dari tanggal yang dimasukkan
        nama_hari = waktu.strftime("%A")

        print("Tanggal yang dimasukkan adalah:", waktu.strftime("%d %B %Y"))
        print("Hari:", nama_hari)
        print("Jam:", waktu.strftime("%H:%M:%S"))
    except ValueError:
        print("Input tidak valid. Pastikan format tanggal dan jam benar (YYYY-MM-DD dan HH:MM:SS).")

if __name__ == "__main__":
    main()
