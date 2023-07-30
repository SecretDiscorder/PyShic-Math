def main():
    input_bilangan = input("Masukkan bilangan acak (pisahkan dengan spasi): ")
    bilangan_list = [int(bil) for bil in input_bilangan.split()]

    if not bilangan_list:
        print("Tidak ada bilangan yang dimasukkan.")
        return

    # Mengurutkan bilangan dari yang terbesar ke terkecil
    urutan_terbesar = sorted(bilangan_list, reverse=True)

    # Mengurutkan bilangan dari yang terkecil ke terbesar
    urutan_terkecil = sorted(bilangan_list)

    print("Urutan bilangan dari yang terbesar:")
    print(urutan_terbesar)

    print("Urutan bilangan dari yang terkecil:")
    print(urutan_terkecil)

if __name__ == "__main__":
    main()

while True:
    main()