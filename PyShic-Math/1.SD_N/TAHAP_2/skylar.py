# Function to compare two fractions
def compare_fractions(numerator1, denominator1, numerator2, denominator2):
    value1 = numerator1 / denominator1
    value2 = numerator2 / denominator2
    if value1 > value2:
        return f"{numerator1}/{denominator1} is greater than {numerator2}/{denominator2}."
    elif value1 < value2:
        return f"{numerator1}/{denominator1} is less than {numerator2}/{denominator2}."
    else:
        return f"{numerator1}/{denominator1} is equal to {numerator2}/{denominator2}."

# Function to find the ratio between two values
def find_ratio(value1, value2):
    ratio = value1 / value2
    return ratio

# Function to scale a value
def scale_value(value, scale_factor):
    scaled_value = value * scale_factor
    return scaled_value

def main_perbandingan_skala():
    print("1. Compare fractions")
    print("2. Find the ratio between two values")
    print("3. Scale a value")
    pilihan = int(input("Enter your choice (1/2/3): "))

    if pilihan == 1:
        numerator1 = float(input("Enter the numerator of the first fraction: "))
        denominator1 = float(input("Enter the denominator of the first fraction: "))
        numerator2 = float(input("Enter the numerator of the second fraction: "))
        denominator2 = float(input("Enter the denominator of the second fraction: "))
        result = compare_fractions(numerator1, denominator1, numerator2, denominator2)
        print(result)

    elif pilihan == 2:
        value1 = float(input("Enter the first value: "))
        value2 = float(input("Enter the second value: "))
        ratio = find_ratio(value1, value2)
        print(f"The ratio of {value1} to {value2} is {ratio}.")

    elif pilihan == 3:
        value = float(input("Enter the value: "))
        scale_factor = float(input("Enter the scale factor: "))
        scaled_value = scale_value(value, scale_factor)
        print(f"The scaled value is {scaled_value}.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_perbandingan_skala()
