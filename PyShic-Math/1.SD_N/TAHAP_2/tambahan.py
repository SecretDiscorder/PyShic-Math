import math

# Function to perform mixed arithmetic operations with integers
def mixed_operations(a, b, c):
    result = a + b * c - a // b
    return result

# Function to find the Greatest Common Divisor (GCD) using the Euclidean algorithm
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Function to find the Least Common Multiple (LCM) of two numbers
def find_lcm(a, b):
    lcm = abs(a * b) // find_gcd(a, b)
    return lcm

# Function to find the Greatest Common Divisor (GCD) of three numbers
def find_gcd_three(a, b, c):
    return find_gcd(a, find_gcd(b, c))

# Function to calculate the cube root of a number
def cube_root(number):
    return number ** (1/3)

def main_operasi_hitung():
    print("1. Perform Mixed Arithmetic Operations with Integers")
    print("2. Find Greatest Common Divisor (GCD) of Two Numbers")
    print("3. Find Least Common Multiple (LCM) of Two Numbers")
    print("4. Find Greatest Common Divisor (GCD) of Three Numbers")
    print("5. Calculate Cube Root of a Number")
    pilihan = int(input("Enter your choice (1/2/3/4/5): "))

    if pilihan == 1:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        result = mixed_operations(a, b, c)
        print(f"The result of the mixed arithmetic operation is: {result}")

    elif pilihan == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        gcd = find_gcd(a, b)
        print(f"The Greatest Common Divisor (GCD) of {a} and {b} is: {gcd}")

    elif pilihan == 3:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        lcm = find_lcm(a, b)
        print(f"The Least Common Multiple (LCM) of {a} and {b} is: {lcm}")

    elif pilihan == 4:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = int(input("Enter the third number: "))
        gcd = find_gcd_three(a, b, c)
        print(f"The Greatest Common Divisor (GCD) of {a}, {b}, and {c} is: {gcd}")

    elif pilihan == 5:
        number = int(input("Enter the number: "))
        cube_root_val = cube_root(number)
        print(f"The cube root of {number} is: {cube_root_val}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_operasi_hitung()
