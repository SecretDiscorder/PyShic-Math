from fractions import Fraction

# Function to compare two fractions
def compare_fractions(a, b):
    if a < b:
        return f"{a} < {b}"
    elif a > b:
        return f"{a} > {b}"
    else:
        return f"{a} = {b}"

# Function to sort a list of fractions
def sort_fractions(fractions):
    return sorted(fractions)

# Function to simplify a fraction
def simplify_fraction(fraction):
    return fraction.__str__()

# Function to perform addition on fractions
def addition_fractions(a, b):
    return a + b

# Function to perform subtraction on fractions
def subtraction_fractions(a, b):
    return a - b

def main_pecahan():
    print("1. Compare two fractions")
    print("2. Sort a list of fractions")
    print("3. Simplify a fraction")
    print("4. Perform addition on fractions")
    print("5. Perform subtraction on fractions")
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))

    if pilihan == 1:
        a = Fraction(input("Masukkan pecahan pertama (misal: 1/2): "))
        b = Fraction(input("Masukkan pecahan kedua (misal: 3/4): "))
        result = compare_fractions(a, b)
        print(result)

    elif pilihan == 2:
        fractions_input = input("Masukkan pecahan, pisahkan dengan spasi (misal: 1/3 2/5 1/4): ").split()
        fractions = [Fraction(f) for f in fractions_input]
        sorted_fractions = sort_fractions(fractions)
        print(f"Pecahan setelah diurutkan: {[frac.__str__() for frac in sorted_fractions]}")

    elif pilihan == 3:
        fraction_input = input("Masukkan pecahan (misal: 6/9): ")
        fraction = Fraction(fraction_input)
        simplified_fraction = simplify_fraction(fraction)
        print(f"Pecahan setelah disederhanakan: {simplified_fraction}")

    elif pilihan == 4:
        a = Fraction(input("Masukkan pecahan pertama (misal: 1/2): "))
        b = Fraction(input("Masukkan pecahan kedua (misal: 3/4): "))
        result = addition_fractions(a, b)
        print(f"{a} + {b} = {result}")

    elif pilihan == 5:
        a = Fraction(input("Masukkan pecahan pertama (misal: 1/2): "))
        b = Fraction(input("Masukkan pecahan kedua (misal: 3/4): "))
        result = subtraction_fractions(a, b)
        print(f"{a} - {b} = {result}")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_pecahan()
