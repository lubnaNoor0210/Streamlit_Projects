sentence: str = "I love to take a walk everymornig. It is the best activity for a healthy life. I love to walk in the jungle."
 
def main():
    adjective = input("Enter an adjective:")
    noun = input("Enter a noun:")
    verb =  input("Enter a verb:")
    print(sentence + adjective + noun + verb + "!")

if __name__ == '__main__':
    main()