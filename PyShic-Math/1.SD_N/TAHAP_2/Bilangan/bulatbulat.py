# Function to calculate the absolute value of an integer
def absolute_value(n):
    return abs(n)

# Function to round a number to the nearest integer
def round_number(n):
    return round(n)

# Function to estimate the result of an arithmetic operation
def estimate_result(op, a, b):
    if op == "+":
        return round_number(a + b)
    elif op == "-":
        return round_number(a - b)
    elif op == "*":
        return round_number(a * b)
    elif op == "/":
        return round_number(a / b)
    else:
        return None

# Function to find the Greatest Common Divisor (GCD) of two integers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Function to find the Least Common Multiple (LCM) of two integers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function to calculate the result of a mixed operation
def mixed_operation(a, b, c, d):
    result = a + b * c / d
    return round_number(result)

# Function to calculate the exponentiation (power) of an integer
def exponentiation(base, exponent):
    return base ** exponent

# Function to calculate the square root of an integer
def square_root(n):
    return n ** 0.5

def main_bilangan_bulat():
    print("1. Calculate absolute value")
    print("2. Round a number")
    print("3. Estimate result of an arithmetic operation")
    print("4. Find Greatest Common Divisor (GCD)")
    print("5. Find Least Common Multiple (LCM)")
    print("6. Perform mixed operation")
    print("7. Calculate exponentiation (power)")
    print("8. Calculate square root")
    pilihan = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))

    if pilihan == 1:
        n = int(input("Enter an integer: "))
        print(f"Absolute value: {absolute_value(n)}")

    elif pilihan == 2:
        n = float(input("Enter a number: "))
        print(f"Rounded number: {round_number(n)}")

    elif pilihan == 3:
        op = input("Enter the arithmetic operation (+, -, *, /): ")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"Estimated result: {estimate_result(op, a, b)}")

    elif pilihan == 4:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        print(f"GCD: {gcd(a, b)}")

    elif pilihan == 5:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        print(f"LCM: {lcm(a, b)}")

    elif pilihan == 6:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        c = int(input("Enter the third integer: "))
        d = int(input("Enter the fourth integer: "))
        print(f"Result of mixed operation: {mixed_operation(a, b, c, d)}")

    elif pilihan == 7:
        base = int(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
        print(f"Exponentiation result: {exponentiation(base, exponent)}")

    elif pilihan == 8:
        n = int(input("Enter an integer: "))
        print(f"Square root: {square_root(n)}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_bilangan_bulat()
