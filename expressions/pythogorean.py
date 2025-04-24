import math
def main():
    print("'Pythogora's Theorem🔼'")

    ab: float = float(input("Enter the value of AB:"))
    ac: float = float(input("Enter the value of AC:"))
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))
if __name__ == '__main__':
    main()
