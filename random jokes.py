import random

def random_joke_generator():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Python programmers prefer using snakes? Because they can’t find the ‘import’ button!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why do Java developers wear glasses? Because they don't see sharp!",
        "Why was the developer unhappy at their job? They wanted arrays!",
        "What do you call a snake that works for the government? A civil serpent!",
        "Why did the programmer quit their job? Because they didn't get arrays!",
        "Why do programmers hate nature? It has too many bugs!",
        "What is a programmer's favorite hangout place? Foo Bar!",
        "Why did the computer go to therapy? Because it had too many bytes!"
    ]

    # Randomly select a joke
    selected_joke = random.choice(jokes)
    return selected_joke

def main():
    print("Welcome to the Random Joke Generator! 🤣")
    print("Here's a programming joke for you:\n")
    print(random_joke_generator())

if __name__ == "__main__":
    main()