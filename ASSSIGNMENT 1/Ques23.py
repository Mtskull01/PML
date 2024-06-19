# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Get the choice and temperature from the user
choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")
temperature = float(input("Enter the temperature to convert: "))

if choice.upper() == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(temperature,"°C is equal to",converted_temperature,"°F")
elif choice.upper() == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(temperature,"°F is equal to",converted_temperature,"°C")
else:
    print("Invalid choice.Please enter 'C' or 'F'.")
