# Sifat Pertukaran/Komutatif
def sifat_pertukaran(operator, a, b):
    if operator == "+":
        return a + b == b + a
    elif operator == "-":
        return a - b == b - a
    elif operator == "*":
        return a * b == b * a
    elif operator == "/":
        return a / b == b / a
    else:
        return False

# Sifat Pengelompokan/Asosiatif
def sifat_pengelompokan(operator, a, b, c):
    if operator == "+" or operator == "-":
        return (a + b) + c == a + (b + c)
    elif operator == "*" or operator == "/":
        return (a * b) * c == a * (b * c)
    else:
        return False

# Sifat Penyebaran/Distributif
def sifat_penyebaran(operator1, operator2, a, b, c):
    if (operator1 == "+" and operator2 == "*") or (operator1 == "*" and operator2 == "+"):
        return a * (b + c) == (a * b) + (a * c)
    elif (operator1 == "-" and operator2 == "*") or (operator1 == "*" and operator2 == "-"):
        return a * (b - c) == (a * b) - (a * c)
    elif (operator1 == "+" and operator2 == "/") or (operator1 == "/" and operator2 == "+"):
        return a / (b + c) == (a / b) + (a / c)
    elif (operator1 == "-" and operator2 == "/") or (operator1 == "/" and operator2 == "-"):
        return a / (b - c) == (a / b) - (a / c)
    else:
        return False

def main_operasi_hitung():
    print("Operasi Hitung dan Sifat-Sifatnya")
    print("1. Sifat Pertukaran/Komutatif")
    print("2. Sifat Pengelompokan/Asosiatif")
    print("3. Sifat Penyebaran/Distributif")
    pilihan = int(input("Masukkan pilihan (1/2/3): "))

    if pilihan == 1:
        operator = input("Masukkan operator (+, -, *, /): ")
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print(f"Sifat Pertukaran/Komutatif {operator}: {sifat_pertukaran(operator, a, b)}")

    elif pilihan == 2:
        operator = input("Masukkan operator (+, -, *, /): ")
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        c = float(input("Masukkan bilangan ketiga: "))
        print(f"Sifat Pengelompokan/Asosiatif {operator}: {sifat_pengelompokan(operator, a, b, c)}")

    elif pilihan == 3:
        operator1 = input("Masukkan operator pertama (+, -, *, /): ")
        operator2 = input("Masukkan operator kedua (+, -, *, /): ")
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        c = float(input("Masukkan bilangan ketiga: "))
        print(f"Sifat Penyebaran/Distributif {operator1} dan {operator2}: {sifat_penyebaran(operator1, operator2, a, b, c)}")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_operasi_hitung()
