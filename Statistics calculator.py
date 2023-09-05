import numpy as np
import statistics

def print_menu():
    print("\nStatistical Analysis Tool Menu:")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Mode")
    print("4. Calculate Variance")
    print("5. Calculate Standard Deviation")
    print("6. Quit")

def calculate_mean(data):
    return np.mean(data)

def calculate_median(data):
    return np.median(data)

def calculate_mode(data):
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        return "No unique mode found"

def calculate_variance(data):
    return np.var(data)

def calculate_standard_deviation(data):
    return np.std(data)

while True:
    print_menu()
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        data = list(map(float, input("Enter data points (comma-separated): ").split(",")))
        mean = calculate_mean(data)
        print(f"Mean: {mean:.2f}")
    elif choice == "2":
        data = list(map(float, input("Enter data points (comma-separated): ").split(",")))
        median = calculate_median(data)
        print(f"Median: {median:.2f}")
    elif choice == "3":
        data = list(map(float, input("Enter data points (comma-separated): ").split(",")))
        mode = calculate_mode(data)
        print(f"Mode: {mode}")
    elif choice == "4":
        data = list(map(float, input("Enter data points (comma-separated): ").split(",")))
        variance = calculate_variance(data)
        print(f"Variance: {variance:.2f}")
    elif choice == "5":
        data = list(map(float, input("Enter data points (comma-separated): ").split(",")))
        std_deviation = calculate_standard_deviation(data)
        print(f"Standard Deviation: {std_deviation:.2f}")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
