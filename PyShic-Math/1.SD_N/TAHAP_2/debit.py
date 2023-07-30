# Function to calculate flow rate (debit) given volume and time
def calculate_flow_rate(volume, time):
    if time == 0:
        return "Time cannot be zero. Division by zero is not allowed."
    flow_rate = volume / time
    return flow_rate

# Function to convert flow rate from one unit to another
def convert_flow_rate(flow_rate, from_unit, to_unit):
    units = {
        "L/s": 1,
        "m3/s": 1000,
        "L/min": 1 / 60,
        "m3/min": 1000 / 60,
        "L/h": 1 / 3600,
        "m3/h": 1000 / 3600,
    }

    if from_unit in units and to_unit in units:
        converted_flow_rate = flow_rate * units[from_unit] / units[to_unit]
        return converted_flow_rate
    else:
        return "Invalid units. Supported units: L/s, m3/s, L/min, m3/min, L/h, m3/h"

def main_pengukuran_volume_per_waktu():
    print("1. Calculate Flow Rate (Debit)")
    print("2. Convert Flow Rate Units")
    pilihan = int(input("Enter your choice (1/2): "))

    if pilihan == 1:
        volume = float(input("Enter the volume in cubic meters (m3): "))
        time = float(input("Enter the time in seconds: "))
        flow_rate = calculate_flow_rate(volume, time)
        print(f"The flow rate (debit) is: {flow_rate} m3/s")

    elif pilihan == 2:
        flow_rate = float(input("Enter the flow rate value: "))
        from_unit = input("Enter the current unit (L/s, m3/s, L/min, m3/min, L/h, m3/h): ")
        to_unit = input("Enter the target unit (L/s, m3/s, L/min, m3/min, L/h, m3/h): ")
        converted_flow_rate = convert_flow_rate(flow_rate, from_unit, to_unit)
        print(f"The converted flow rate is: {converted_flow_rate} {to_unit}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_pengukuran_volume_per_waktu()
