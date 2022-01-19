# --------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your choice (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
# --------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0


# --------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("Results")
    print("--------------------------------")


    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# --------------------------------
def play_again():

    response = input("Would you like to take the quiz again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# --------------------------------

questions = {
    "What color is the space stone?: ": "A",
    "How many Iron Man movies have been released?: ": "B",
    "Who is Thor's father?: ": "C",
    "What is the first name of Dr. Strange?: ": "A"
}

options = [["A. Blue", "B. Purple", "C. Red", "D. Yellow"],
           ["A. 4", "B. 3", "C. 2", "D. 5"],
           ["A. Loki", "B. Stark", "C. Odin", "D. Zeus"],
           ["A. Stephen", "B. Steven", "C. Tony", "D. Craig"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")






