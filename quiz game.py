def quiz_game():
    questions = [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["1", "2", "8", "3"],
            "answer": "8"
        },
        {
            "question": "Which of the following is a Python tuple?",
            "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "None of the above"],
            "answer": "(1, 2, 3)"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["function", "def", "define", "fun"],
            "answer": "def"
        },
        {
            "question": "Which of the following is not a valid variable name in Python?",
            "options": ["my_var", "my-var", "myVar", "_myvar"],
            "answer": "my-var"
        },
        {
            "question": "What is the correct way to create a list in Python?",
            "options": ["[]", "{}", "()"],
            "answer": "[]"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        
        answer = input("Please enter the number of your answer: ")
        
        # Check if the answer is valid
        if answer.isdigit() and 1 <= int(answer) <= len(q["options"]):
            selected_option = q["options"][int(answer) - 1]
            if selected_option == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}\n")
        else:
            print("Invalid input. Please enter a number corresponding to the options.\n")

    print(f"Your final score is: {score}/{len(questions)}")

def main():
    while True:
        quiz_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(" You are a Guru, Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()