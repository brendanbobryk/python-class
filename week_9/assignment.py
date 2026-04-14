def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def main() -> None:
    print("Excercise 1:\n---------------")
    f = float(input("Enter temperature in Fahrenheit: "))
    c_converted = fahrenheit_to_celsius(f)
    print(f"Temperature in Celsius: {c_converted:.2f}")

    print("\nExcercise 2:\n---------------")
    c = float(input("Enter temperature in Celsius: "))
    f_converted = celsius_to_fahrenheit(c)
    print(f"Temperature in Fahrenheit: {f_converted:.2f}")

    print("\nExcercise 3:\n---------------")
    print(f"Fahrenheit: {f}\tCelsius: {c_converted:.2f}")
    print(f"Celsius: {c}   \tFahrenheit: {f_converted:.2f}")

main()