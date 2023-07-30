def hitung_banyak_benda(daftar_benda, benda_dicari):
    count = 0
    for benda in daftar_benda:
        if benda == benda_dicari:
            count += 1
    return count

def main():
    # Meminta pengguna memasukkan daftar benda
    daftar_benda = input("Masukkan daftar benda (pisahkan dengan koma): ").split(',')
    # Membersihkan whitespace pada elemen daftar benda
    daftar_benda = [item.strip() for item in daftar_benda]

    # Meminta pengguna memasukkan benda yang akan dicari
    benda_dicari = input("Masukkan nama benda yang akan dicari: ")

    banyak_benda = hitung_banyak_benda(daftar_benda, benda_dicari)
    print(f"Banyaknya {benda_dicari} dalam daftar: {banyak_benda}")

if __name__ == "__main__":
    main()

while True:
    main()