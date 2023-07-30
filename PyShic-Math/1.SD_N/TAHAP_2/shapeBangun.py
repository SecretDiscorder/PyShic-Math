# Function to calculate the surface area of a cuboid (balok)
def surface_area_cuboid(length, width, height):
    return 2 * ((length * width) + (length * height) + (width * height))

# Function to calculate the volume of a cuboid (balok)
def volume_cuboid(length, width, height):
    return length * width * height

# Function to calculate the surface area of a cube (kubus)
def surface_area_cube(side):
    return 6 * (side ** 2)

# Function to calculate the volume of a cube (kubus)
def volume_cube(side):
    return side ** 3

# Function to generate the net (unfolded shape) of a cuboid
def net_cuboid(length, width, height):
    top_bottom = length * width
    front_back = width * height
    left_right = length * height
    return [top_bottom, front_back, left_right]

# Function to generate the net (unfolded shape) of a cube
def net_cube(side):
    return [side ** 2]

# Function to check if a 2D shape has line (fold) symmetry
def has_line_symmetry(shape):
    n = len(shape)
    for i in range(n // 2):
        if shape[i] != shape[n - 1 - i]:
            return False
    return True

# Function to check if a 2D shape has rotational symmetry
def has_rotational_symmetry(shape):
    n = len(shape)
    for i in range(1, n):
        if shape[i:] + shape[:i] == shape:
            return True
    return False

# Function to perform reflection (mirroring) on a 2D shape
def reflection(shape):
    n = len(shape)
    reflected_shape = [0] * n
    for i in range(n):
        reflected_shape[i] = shape[n - 1 - i]
    return reflected_shape

def main_bangun_ruang():
    print("1. Calculate surface area and volume of a cuboid")
    print("2. Calculate surface area and volume of a cube")
    print("3. Generate net of a cuboid")
    print("4. Generate net of a cube")
    print("5. Check for line (fold) symmetry")
    print("6. Check for rotational symmetry")
    print("7. Perform reflection (mirroring)")
    pilihan = int(input("Enter your choice (1/2/3/4/5/6/7): "))

    if pilihan == 1:
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        print(f"Surface area: {surface_area_cuboid(length, width, height)}")
        print(f"Volume: {volume_cuboid(length, width, height)}")

    elif pilihan == 2:
        side = float(input("Enter the side length of the cube: "))
        print(f"Surface area: {surface_area_cube(side)}")
        print(f"Volume: {volume_cube(side)}")

    elif pilihan == 3:
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        net = net_cuboid(length, width, height)
        print(f"Net of the cuboid: {net}")

    elif pilihan == 4:
        side = float(input("Enter the side length of the cube: "))
        net = net_cube(side)
        print(f"Net of the cube: {net}")

    elif pilihan == 5:
        shape = input("Enter the 2D shape (e.g., 'ABCD'): ")
        if has_line_symmetry(shape):
            print("The shape has line (fold) symmetry.")
        else:
            print("The shape does not have line (fold) symmetry.")

    elif pilihan == 6:
        shape = input("Enter the 2D shape (e.g., 'ABCD'): ")
        if has_rotational_symmetry(shape):
            print("The shape has rotational symmetry.")
        else:
            print("The shape does not have rotational symmetry.")

    elif pilihan == 7:
        shape = input("Enter the 2D shape (e.g., 'ABCD'): ")
        reflected_shape = reflection(shape)
        print(f"Reflected shape: {reflected_shape}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_bangun_ruang()
