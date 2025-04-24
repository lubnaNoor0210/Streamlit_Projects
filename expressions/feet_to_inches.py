INCHES_IN_FOOT = 12

def main():
    print("Convert Inches to Feet")
    print("------------------------")
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_IN_FOOT
    print(f"That is {inches} inches")

if __name__ == '__main__':
    main()