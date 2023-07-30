# Function to convert fraction to percentage
def fraction_to_percentage(numerator, denominator):
    percentage = (numerator / denominator) * 100
    return percentage

# Function to convert fraction to decimal
def fraction_to_decimal(numerator, denominator):
    decimal = numerator / denominator
    return decimal

# Function to add fractions
def add_fractions(numerator1, denominator1, numerator2, denominator2):
    result_numerator = (numerator1 * denominator2) + (numerator2 * denominator1)
    result_denominator = denominator1 * denominator2
    return result_numerator, result_denominator

# Function to subtract fractions
def subtract_fractions(numerator1, denominator1, numerator2, denominator2):
    result_numerator = (numerator1 * denominator2) - (numerator2 * denominator1)
    result_denominator = denominator1 * denominator2
    return result_numerator, result_denominator

# Function to multiply fractions
def multiply_fractions(numerator1, denominator1, numerator2, denominator2):
    result_numerator = numerator1 * numerator2
    result_denominator = denominator1 * denominator2
    return result_numerator, result_denominator

# Function to divide fractions
def divide_fractions(numerator1, denominator1, numerator2, denominator2):
    result_numerator = numerator1 * denominator2
    result_denominator = denominator1 * numerator2
    return result_numerator, result_denominator

def main_pecahan():
    print("1. Convert fraction to percentage and decimal")
    print("2. Add fractions")
    print("3. Subtract fractions")
    print("4. Multiply fractions")
    print("5. Divide fractions")
    pilihan = int(input("Enter your choice (1/2/3/4/5): "))

    if pilihan == 1:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        percentage = fraction_to_percentage(numerator, denominator)
        decimal = fraction_to_decimal(numerator, denominator)
        print(f"The fraction {numerator}/{denominator} is equal to {percentage:.2f}% and {decimal:.2f} as a decimal.")

    elif pilihan in [2, 3, 4, 5]:
        numerator1 = float(input("Enter the numerator of the first fraction: "))
        denominator1 = float(input("Enter the denominator of the first fraction: "))
        numerator2 = float(input("Enter the numerator of the second fraction: "))
        denominator2 = float(input("Enter the denominator of the second fraction: "))

        if pilihan == 2:
            result_numerator, result_denominator = add_fractions(numerator1, denominator1, numerator2, denominator2)
            operation = "added to"
        elif pilihan == 3:
            result_numerator, result_denominator = subtract_fractions(numerator1, denominator1, numerator2, denominator2)
            operation = "subtracted from"
        elif pilihan == 4:
            result_numerator, result_denominator = multiply_fractions(numerator1, denominator1, numerator2, denominator2)
            operation = "multiplied by"
        else:
            result_numerator, result_denominator = divide_fractions(numerator1, denominator1, numerator2, denominator2)
            operation = "divided by"

        print(f"The result of {numerator1}/{denominator1} {operation} {numerator2}/{denominator2} is {result_numerator}/{result_denominator}.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_pecahan()
