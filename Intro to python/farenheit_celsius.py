def main():
    farenheit = float(input("Enter temperature in Farenheit:"))
    celsius = (farenheit - 32) * 5.0 / 9.0
    print(f"temperature: {farenheit}F = {celsius}C")
main()