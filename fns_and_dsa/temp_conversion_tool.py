# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Conversion functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main function for user interaction
def main():
    print("Temperature Conversion Tool")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    choice = input("Choose an option (1 or 2): ")

    try:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
