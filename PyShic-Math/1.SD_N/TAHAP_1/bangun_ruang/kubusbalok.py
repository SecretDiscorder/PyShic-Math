# Function to calculate the volume of a cube
def calculate_volume_cube(side):
    volume = side ** 3
    return volume

# Function to calculate the volume of a rectangular cuboid (balok)
def calculate_volume_balok(length, width, height):
    volume = length * width * height
    return volume

def main_volume_kubus_dan_balok():
    print("1. Calculate the volume of a cube")
    print("2. Calculate the volume of a rectangular cuboid (balok)")
    pilihan = int(input("Enter your choice (1/2): "))

    if pilihan == 1:
        side = float(input("Enter the length of a side of the cube: "))
        volume_cube = calculate_volume_cube(side)
        print(f"The volume of the cube is {volume_cube} cubic units.")

    elif pilihan == 2:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        volume_balok = calculate_volume_balok(length, width, height)
        print(f"The volume of the rectangular cuboid (balok) is {volume_balok} cubic units.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_volume_kubus_dan_balok()
