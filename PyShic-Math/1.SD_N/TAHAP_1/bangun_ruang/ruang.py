import math

# Function to calculate the area of a square
def calculate_area_square(side_length):
    return side_length * side_length

# Function to calculate the area of a rectangle
def calculate_area_rectangle(length, width):
    return length * width

# Function to calculate the area of a triangle
def calculate_area_triangle(base, height):
    return 0.5 * base * height

# Function to calculate the area of a regular polygon (n-sided shape)
def calculate_area_regular_polygon(side_length, num_sides):
    perimeter = side_length * num_sides
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    return 0.5 * perimeter * apothem

# Function to calculate the area of a circle
def calculate_area_circle(radius):
    return math.pi * radius ** 2

# Function to calculate the volume of a triangular prism
def calculate_volume_triangular_prism(base_area, height):
    return base_area * height

# Function to calculate the volume of a cylinder
def calculate_volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def main_menghitung_luas():
    print("1. Calculate the Area of a Square")
    print("2. Calculate the Area of a Rectangle")
    print("3. Calculate the Area of a Triangle")
    print("4. Calculate the Area of a Regular Polygon")
    print("5. Calculate the Area of a Circle")
    print("6. Calculate the Volume of a Triangular Prism")
    print("7. Calculate the Volume of a Cylinder")
    pilihan = int(input("Enter your choice (1/2/3/4/5/6/7): "))

    if pilihan == 1:
        side_length = float(input("Enter the side length of the square: "))
        area = calculate_area_square(side_length)
        print(f"The area of the square is: {area}")

    elif pilihan == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")

    elif pilihan == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_area_triangle(base, height)
        print(f"The area of the triangle is: {area}")

    elif pilihan == 4:
        side_length = float(input("Enter the side length of the regular polygon: "))
        num_sides = int(input("Enter the number of sides of the regular polygon: "))
        area = calculate_area_regular_polygon(side_length, num_sides)
        print(f"The area of the regular polygon is: {area}")

    elif pilihan == 5:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area_circle(radius)
        print(f"The area of the circle is: {area}")

    elif pilihan == 6:
        base_area = float(input("Enter the base area of the triangular prism: "))
        height = float(input("Enter the height of the triangular prism: "))
        volume = calculate_volume_triangular_prism(base_area, height)
        print(f"The volume of the triangular prism is: {volume}")

    elif pilihan == 7:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = calculate_volume_cylinder(radius, height)
        print(f"The volume of the cylinder is: {volume}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_menghitung_luas()
