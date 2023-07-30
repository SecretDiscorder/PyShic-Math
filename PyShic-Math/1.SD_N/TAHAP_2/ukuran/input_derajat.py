# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * (3.14159265358979323846 / 180)

# Function to convert radians to degrees
def radians_to_degrees(radians):
    return radians * (180 / 3.14159265358979323846)

# Function to convert time in hours and minutes to minutes
def time_to_minutes(hours, minutes):
    return hours * 60 + minutes

# Function to convert time in minutes to hours and minutes
def minutes_to_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes

# Function to convert weight in grams to kilograms
def grams_to_kilograms(grams):
    return grams / 1000

# Function to convert weight in kilograms to grams
def kilograms_to_grams(kilograms):
    return kilograms * 1000

# Function to convert length in centimeters to meters
def centimeters_to_meters(centimeters):
    return centimeters / 100

# Function to convert length in meters to centimeters
def meters_to_centimeters(meters):
    return meters * 100

def main_pengukuran():
    print("1. Convert Degrees to Radians")
    print("2. Convert Radians to Degrees")
    print("3. Convert Time to Minutes")
    print("4. Convert Minutes to Time")
    print("5. Convert Grams to Kilograms")
    print("6. Convert Kilograms to Grams")
    print("7. Convert Centimeters to Meters")
    print("8. Convert Meters to Centimeters")
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6/7/8): "))

    if pilihan == 1:
        degrees = float(input("Masukkan besar sudut dalam derajat: "))
        radians = degrees_to_radians(degrees)
        print(f"{degrees} derajat setara dengan {radians:.2f} radians.")

    elif pilihan == 2:
        radians = float(input("Masukkan besar sudut dalam radians: "))
        degrees = radians_to_degrees(radians)
        print(f"{radians} radians setara dengan {degrees:.2f} derajat.")

    elif pilihan == 3:
        hours = int(input("Masukkan jam: "))
        minutes = int(input("Masukkan menit: "))
        total_minutes = time_to_minutes(hours, minutes)
        print(f"{hours} jam {minutes} menit setara dengan {total_minutes} menit.")

    elif pilihan == 4:
        total_minutes = int(input("Masukkan total menit: "))
        hours, minutes = minutes_to_time(total_minutes)
        print(f"{total_minutes} menit setara dengan {hours} jam {minutes} menit.")

    elif pilihan == 5:
        grams = float(input("Masukkan berat dalam gram: "))
        kilograms = grams_to_kilograms(grams)
        print(f"{grams} gram setara dengan {kilograms:.2f} kilogram.")

    elif pilihan == 6:
        kilograms = float(input("Masukkan berat dalam kilogram: "))
        grams = kilograms_to_grams(kilograms)
        print(f"{kilograms} kilogram setara dengan {grams:.2f} gram.")

    elif pilihan == 7:
        centimeters = float(input("Masukkan panjang dalam sentimeter: "))
        meters = centimeters_to_meters(centimeters)
        print(f"{centimeters} sentimeter setara dengan {meters:.2f} meter.")

    elif pilihan == 8:
        meters = float(input("Masukkan panjang dalam meter: "))
        centimeters = meters_to_centimeters(meters)
        print(f"{meters} meter setara dengan {centimeters:.2f} sentimeter.")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_pengukuran()
