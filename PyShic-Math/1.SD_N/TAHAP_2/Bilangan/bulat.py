# Function to compare two integers
def compare_integers(a, b):
    if a < b:
        return f"{a} < {b}"
    elif a > b:
        return f"{a} > {b}"
    else:
        return f"{a} = {b}"

# Function to sort a list of integers in ascending order
def sort_integers(numbers):
    return sorted(numbers)

# Function to find the opposite of an integer
def opposite_integer(a):
    return -a

# Function to perform addition on integers
def addition(a, b):
    return a + b

# Function to perform subtraction on integers
def subtraction(a, b):
    return a - b

def main_bilangan_bulat():
    print("1. Compare two integers")
    print("2. Sort a list of integers")
    print("3. Find the opposite of an integer")
    print("4. Perform addition on integers")
    print("5. Perform subtraction on integers")
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))

    if pilihan == 1:
        a = int(input("Masukkan bilangan bulat pertama: "))
        b = int(input("Masukkan bilangan bulat kedua: "))
        result = compare_integers(a, b)
        print(result)

    elif pilihan == 2:
        numbers = list(map(int, input("Masukkan bilangan bulat, pisahkan dengan spasi: ").split()))
        sorted_numbers = sort_integers(numbers)
        print(f"Bilangan bulat setelah diurutkan: {sorted_numbers}")

    elif pilihan == 3:
        a = int(input("Masukkan bilangan bulat: "))
        opposite = opposite_integer(a)
        print(f"Lawan dari {a} adalah {opposite}")

    elif pilihan == 4:
        a = int(input("Masukkan bilangan bulat pertama: "))
        b = int(input("Masukkan bilangan bulat kedua: "))
        result = addition(a, b)
        print(f"{a} + {b} = {result}")

    elif pilihan == 5:
        a = int(input("Masukkan bilangan bulat pertama: "))
        b = int(input("Masukkan bilangan bulat kedua: "))
        result = subtraction(a, b)
        print(f"{a} - {b} = {result}")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_bilangan_bulat()
