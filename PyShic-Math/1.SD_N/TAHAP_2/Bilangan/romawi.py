# Dictionary to map Roman numerals to integers
roman_to_int = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

# Function to convert Roman numerals to integers
def roman_to_integer(roman_numeral):
    total = 0
    prev_value = 0

    for numeral in reversed(roman_numeral):
        value = roman_to_int[numeral]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Function to convert integers to Roman numerals
def integer_to_roman(num):
    roman_numerals = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]

    result = ''
    for symbol, value in roman_numerals:
        while num >= value:
            result += symbol
            num -= value

    return result

def main_bilangan_romawi():
    print("1. Convert Roman numerals to integers")
    print("2. Convert integers to Roman numerals")
    pilihan = int(input("Enter your choice (1/2): "))

    if pilihan == 1:
        roman_numeral = input("Enter a Roman numeral: ")
        integer_value = roman_to_integer(roman_numeral)
        print(f"The integer value of {roman_numeral} is: {integer_value}")

    elif pilihan == 2:
        num = int(input("Enter an integer: "))
        roman_numeral = integer_to_roman(num)
        print(f"The Roman numeral representation of {num} is: {roman_numeral}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_bilangan_romawi()
