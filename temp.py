import sys

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            celsius = float(sys.argv[1])
        else:
            print("No input given - using default value.")
            celsius = 0

        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid numeric value")
