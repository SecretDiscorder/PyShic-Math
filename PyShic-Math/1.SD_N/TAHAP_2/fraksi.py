from fractions import Fraction

# Function to simplify a fraction
def simplify_fraction(numerator, denominator):
    return Fraction(numerator, denominator)

# Function to convert a fraction to a decimal
def fraction_to_decimal(numerator, denominator):
    return float(numerator) / denominator

# Function to convert a decimal to a fraction
def decimal_to_fraction(decimal):
    return Fraction(decimal).limit_denominator()

# Function to add two fractions
def add_fractions(n1, d1, n2, d2):
    return Fraction(n1, d1) + Fraction(n2, d2)

# Function to subtract two fractions
def subtract_fractions(n1, d1, n2, d2):
    return Fraction(n1, d1) - Fraction(n2, d2)

# Function to multiply two fractions
def multiply_fractions(n1, d1, n2, d2):
    return Fraction(n1, d1) * Fraction(n2, d2)

# Function to divide two fractions
def divide_fractions(n1, d1, n2, d2):
    return Fraction(n1, d1) / Fraction(n2, d2)

def main_operasi_hitung_pecahan():
    print("1. Simplify a Fraction")
    print("2. Convert Fraction to Decimal")
    print("3. Convert Decimal to Fraction")
    print("4. Add Fractions")
    print("5. Subtract Fractions")
    print("6. Multiply Fractions")
    print("7. Divide Fractions")
    pilihan = int(input("Enter your choice (1/2/3/4/5/6/7): "))

    if pilihan == 1:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = simplify_fraction(numerator, denominator)
        print(f"The simplified fraction is: {result}")

    elif pilihan == 2:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = fraction_to_decimal(numerator, denominator)
        print(f"The decimal representation is: {result}")

    elif pilihan == 3:
        decimal = float(input("Enter the decimal: "))
        result = decimal_to_fraction(decimal)
        print(f"The fraction representation is: {result}")

    elif pilihan == 4:
        n1 = int(input("Enter the numerator of the first fraction: "))
        d1 = int(input("Enter the denominator of the first fraction: "))
        n2 = int(input("Enter the numerator of the second fraction: "))
        d2 = int(input("Enter the denominator of the second fraction: "))
        result = add_fractions(n1, d1, n2, d2)
        print(f"The result of addition is: {result}")

    elif pilihan == 5:
        n1 = int(input("Enter the numerator of the first fraction: "))
        d1 = int(input("Enter the denominator of the first fraction: "))
        n2 = int(input("Enter the numerator of the second fraction: "))
        d2 = int(input("Enter the denominator of the second fraction: "))
        result = subtract_fractions(n1, d1, n2, d2)
        print(f"The result of subtraction is: {result}")

    elif pilihan == 6:
        n1 = int(input("Enter the numerator of the first fraction: "))
        d1 = int(input("Enter the denominator of the first fraction: "))
        n2 = int(input("Enter the numerator of the second fraction: "))
        d2 = int(input("Enter the denominator of the second fraction: "))
        result = multiply_fractions(n1, d1, n2, d2)
        print(f"The result of multiplication is: {result}")

    elif pilihan == 7:
        n1 = int(input("Enter the numerator of the first fraction: "))
        d1 = int(input("Enter the denominator of the first fraction: "))
        n2 = int(input("Enter the numerator of the second fraction: "))
        d2 = int(input("Enter the denominator of the second fraction: "))
        result = divide_fractions(n1, d1, n2, d2)
        print(f"The result of division is: {result}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_operasi_hitung_pecahan()
