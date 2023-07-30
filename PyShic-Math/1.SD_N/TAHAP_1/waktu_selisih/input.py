from datetime import datetime

def main():
    while True:
        print("\nPilih opsi:")
        print("1. Tampilkan tanggal dan waktu saat ini")
        print("2. Hitung selisih waktu")
        print("3. Keluar")
        
        choice = input("Masukkan pilihan (1/2/3): ")
        
        if choice == '1':
            show_current_datetime()
        elif choice == '2':
            calculate_time_difference()
        elif choice == '3':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def show_current_datetime():
    now = datetime.now()
    print("Tanggal dan waktu saat ini:", now)

def calculate_time_difference():
    try:
        date_format = "%Y-%m-%d %H:%M:%S"

        start_time_str = input("Masukkan waktu awal (format: YYYY-MM-DD HH:MM:SS): ")
        start_time = datetime.strptime(start_time_str, date_format)

        end_time_str = input("Masukkan waktu akhir (format: YYYY-MM-DD HH:MM:SS): ")
        end_time = datetime.strptime(end_time_str, date_format)

        time_difference = end_time - start_time
        print("Selisih waktu:", time_difference)
    except ValueError:
        print("Format waktu tidak valid. Pastikan Anda memasukkan waktu dalam format yang benar.")

if __name__ == "__main__":
    main()
