# Function to convert hours, minutes, and seconds to total seconds
def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

# Function to convert total seconds to hours, minutes, and seconds
def seconds_to_time(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

# Function to measure an angle in degrees and radians
def measure_angle():
    degrees = float(input("Enter the angle in degrees: "))
    radians = degrees * (3.14159265358979323846 / 180)
    print(f"The angle is {degrees} degrees and {radians:.4f} radians.")

# Function to calculate distance given speed and time
def calculate_distance(speed, time):
    distance = speed * time
    return distance

# Function to calculate speed given distance and time
def calculate_speed(distance, time):
    speed = distance / time
    return speed

def main_pengukuran():
    print("1. Convert time to seconds")
    print("2. Convert seconds to time")
    print("3. Measure an angle in degrees and radians")
    print("4. Calculate distance given speed and time")
    print("5. Calculate speed given distance and time")
    pilihan = int(input("Enter your choice (1/2/3/4/5): "))

    if pilihan == 1:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total_seconds = time_to_seconds(hours, minutes, seconds)
        print(f"Total seconds: {total_seconds}")

    elif pilihan == 2:
        total_seconds = int(input("Enter total seconds: "))
        hours, minutes, seconds = seconds_to_time(total_seconds)
        print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")

    elif pilihan == 3:
        measure_angle()

    elif pilihan == 4:
        speed = float(input("Enter the speed (in meters per second): "))
        time = float(input("Enter the time (in seconds): "))
        distance = calculate_distance(speed, time)
        print(f"The distance is {distance} meters.")

    elif pilihan == 5:
        distance = float(input("Enter the distance (in meters): "))
        time = float(input("Enter the time (in seconds): "))
        speed = calculate_speed(distance, time)
        print(f"The speed is {speed} meters per second.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_pengukuran()
