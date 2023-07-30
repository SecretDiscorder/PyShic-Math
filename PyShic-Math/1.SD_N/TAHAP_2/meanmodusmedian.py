def data_presentation(data):
    print("Data:")
    for item in data:
        print(item)

def calculate_mean(data):
    total = sum(data)
    count = len(data)
    mean = total / count
    return mean

def calculate_mode(data):
    frequency = {}
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    max_frequency = max(frequency.values())
    mode = [item for item, freq in frequency.items() if freq == max_frequency]
    return mode

def sort_data(data):
    sorted_data = sorted(data)
    return sorted_data

def find_highest_value(data):
    return max(data)

def find_lowest_value(data):
    return min(data)

def interpret_results(mean, mode, sorted_data, highest_value, lowest_value):
    print(f"\nMean: {mean}")
    print(f"Mode: {mode}")
    print(f"Sorted Data: {sorted_data}")
    print(f"Highest Value: {highest_value}")
    print(f"Lowest Value: {lowest_value}")

def main_pengolahan_data():
    data = []
    n = int(input("Enter the number of data points: "))

    for i in range(n):
        value = float(input(f"Enter data point {i+1}: "))
        data.append(value)

    data_presentation(data)
    mean = calculate_mean(data)
    mode = calculate_mode(data)
    sorted_data = sort_data(data)
    highest_value = find_highest_value(data)
    lowest_value = find_lowest_value(data)

    interpret_results(mean, mode, sorted_data, highest_value, lowest_value)

if __name__ == "__main__":
    main_pengolahan_data()
