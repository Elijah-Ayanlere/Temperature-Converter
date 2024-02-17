import time

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def temperature_converter():
    while True:
        time.sleep(1)
        print("\nTemperature Converter")
        time.sleep(1.5)
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Quit")
        time.sleep(0.5)
        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            time.sleep(1.5)
            print("\nExiting Temperature Converter. Goodbye!")
            break

        if choice in {'1', '2', '3', '4'}:
            time.sleep(0.5)
            temperature = float(input("\nEnter temperature value: "))
            
            if choice == '1':
                result = celsius_to_fahrenheit(temperature)
                print(f"\n{temperature} Celsius is equal to {result} Fahrenheit.")
            elif choice == '2':
                result = fahrenheit_to_celsius(temperature)
                print(f"\n{temperature} Fahrenheit is equal to {result} Celsius.")
            elif choice == '3':
                result = celsius_to_kelvin(temperature)
                print(f"\n{temperature} Celsius is equal to {result} Kelvin.")
            elif choice == '4':
                result = kelvin_to_celsius(temperature)
                print(f"\n{temperature} Kelvin is equal to {result} Celsius.")
        else:
            time.sleep(1.5)
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    temperature_converter()
