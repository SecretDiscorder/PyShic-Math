# Function to find the factors of a number
def faktor_bilangan(bilangan):
    faktor = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            faktor.append(i)
    return faktor

# Function to find the multiples of a number within a range
def kelipatan_bilangan(bilangan, batas_atas):
    kelipatan = []
    for i in range(1, batas_atas + 1):
        kelipatan.append(bilangan * i)
    return kelipatan

# Function to find the greatest common divisor (FPB) of two numbers
def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the least common multiple (KPK) of two numbers
def kpk(a, b):
    return (a * b) // fpb(a, b)

# Function to check if a number is prime
def bilangan_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

# Function to find the prime factors of a number
def faktor_prima(bilangan):
    faktor_prima = []
    divisor = 2
    while bilangan > 1:
        while bilangan % divisor == 0:
            faktor_prima.append(divisor)
            bilangan //= divisor
        divisor += 1
    return faktor_prima

def main_fpb_kpk_bilangan_prima():
    print("1. Faktor Bilangan")
    print("2. Kelipatan Bilangan")
    print("3. Faktor Persekutuan Terbesar (FPB) Dua Bilangan")
    print("4. Faktor Persekutuan Terkecil (KPK) Dua Bilangan")
    print("5. Cek Bilangan Prima")
    print("6. Faktor Prima Dari Suatu Bilangan")
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6): "))

    if pilihan == 1:
        bilangan = int(input("Masukkan bilangan: "))
        faktor = faktor_bilangan(bilangan)
        print(f"Faktor dari {bilangan}: {faktor}")

    elif pilihan == 2:
        bilangan = int(input("Masukkan bilangan: "))
        batas_atas = int(input("Masukkan batas atas: "))
        kelipatan = kelipatan_bilangan(bilangan, batas_atas)
        print(f"Kelipatan dari {bilangan} hingga {batas_atas}: {kelipatan}")

    elif pilihan == 3:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        fpb_result = fpb(a, b)
        print(f"FPB dari {a} dan {b}: {fpb_result}")

    elif pilihan == 4:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        kpk_result = kpk(a, b)
        print(f"KPK dari {a} dan {b}: {kpk_result}")

    elif pilihan == 5:
        bilangan = int(input("Masukkan bilangan: "))
        if bilangan_prima(bilangan):
            print(f"{bilangan} adalah bilangan prima.")
        else:
            print(f"{bilangan} bukan bilangan prima.")

    elif pilihan == 6:
        bilangan = int(input("Masukkan bilangan: "))
        faktor_prima_result = faktor_prima(bilangan)
        print(f"Faktor prima dari {bilangan}: {faktor_prima_result}")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_fpb_kpk_bilangan_prima()
