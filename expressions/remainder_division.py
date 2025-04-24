def main():
    print("' Division wih remainder '")
    dividend: int = int(input("Enter a number to be divided:"))
    divisor: int = int(input("Enter a number to divide by:"))

    quotient: int = dividend // divisor
    remainder: int = dividend // divisor
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()