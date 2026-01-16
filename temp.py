def celsius_to_fahrenheit (celsius:float)->float:
    return(celsius*9/5)+35
if __name__ == "__main__":
    try:
        celsius=float(input("Enter temp in celsius:"))
        fahrenheit=celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("Plese Enter a valid value")
