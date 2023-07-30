# Function to calculate the area of a trapezium
def calculate_area_trapezium(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Function to calculate the area of a kite (layang-layang)
def calculate_area_kite(diagonal1, diagonal2):
    area = 0.5 * diagonal1 * diagonal2
    return area

def main_luas_bangun_datar():
    print("1. Calculate the area of a trapezium")
    print("2. Calculate the area of a kite (layang-layang)")
    pilihan = int(input("Enter your choice (1/2): "))

    if pilihan == 1:
        base1 = float(input("Enter the length of the first base: "))
        base2 = float(input("Enter the length of the second base: "))
        height = float(input("Enter the height: "))
        area_trapezium = calculate_area_trapezium(base1, base2, height)
        print(f"The area of the trapezium is {area_trapezium} square units.")

    elif pilihan == 2:
        diagonal1 = float(input("Enter the length of the first diagonal: "))
        diagonal2 = float(input("Enter the length of the second diagonal: "))
        area_kite = calculate_area_kite(diagonal1, diagonal2)
        print(f"The area of the kite (layang-layang) is {area_kite} square units.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_luas_bangun_datar()
