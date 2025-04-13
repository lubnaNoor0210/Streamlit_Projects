PROMPT = "What do you want?"
JOKE_QUESTION: str = "Why do python developers prefer dark mode?"
JOKE_ANSWER = "Because light attracts bugs."
SORRY= "Sorry! I only tell jokes."

user_input = input(PROMPT).lower() 

if user_input == "joke":
    print(JOKE_QUESTION)
    follow_up = input().lower()
    if follow_up == "why":
        print(JOKE_ANSWER)
    else:
        print("you where supposed to say 'why'!")
else:
    print(SORRY)